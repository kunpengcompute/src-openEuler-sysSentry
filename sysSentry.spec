# Copyright (c) Huawei Technologies Co., Ltd. 2014-2023. All rights reserved.
# Description: spec file for package syssentry

Summary: System Inspection Framework
Name: sysSentry
Version: 1.0.2
Release: 10
License: Mulan PSL v2
Group: System Environment/Daemons
Source0: https://gitee.com/openeuler/sysSentry/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_builddir}/%{name}-root

Patch1:    fix-version-in-setup.py.patch
Patch2:    Fix-the-problem-that-function-cpu_report_result-is-c.patch
Patch3:    fix-error-handling.patch
Patch4:    fix-result-when-process-output-is-None.patch
Patch5:    cpu_utility-and-cpu_patrol-must-be-an-integer.patch
Patch6:    setting-parameters-must-be-integer.patch
Patch7:    param-must-be-integer.patch
Patch8:    add-deleted-code-to-plugin-rasdaemon.patch
Patch9:    Remove-ANSI-escape-sequences.patch
Patch10:   split-cpu_sentry-and-syssentry.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3 python3-setuptools
BuildRequires: json-c-devel
BuildRequires: chrpath
Requires:      libxalarm = %{version}

%description
sysSentry provides framework tools for system inspection.

%package -n libxalarm
Summary:        The xalarm library for the sysSentry
Requires:       json-c
Provides:       libxalarm = %{version}

%description -n libxalarm
This package provides xalarm library for the sysSentry.

%package -n libxalarm-devel
Summary:        The development package for the libxalarm
Requires:       libxalarm = %{version}
Requires:       json-c-devel
Provides:       libxalarm-devel = %{version}

%description -n libxalarm-devel
This package provides developer tools for the libxalarm.

%package -n cpu_sentry
Summary:        CPU fault inspection program
Requires:       procps-ng
Recommends:     sysSentry = %{version}-%{release}
Recommends:     ipmitool

%description -n cpu_sentry
This package provides CPU fault detection

%prep
%autosetup -n %{name}-%{version} -p1

%build
# xalarm
sh build/build.sh -b %{buildroot}%{_libdir}

# sysSentry
pushd src/python
python3 setup.py build
popd

pushd src/c/catcli/catlib
cmake -B ./build/ -S . -D CMAKE_INSTALL_PREFIX=/usr/local -D CMAKE_BUILD_TYPE=Release
pushd build
make
popd
popd

%install
# sysSentry
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_var}/log/sysSentry
install src/python/syssentry/sentryctl %{buildroot}%{_bindir}
install -d -m 700 %{buildroot}/etc/sysSentry/
install -d -m 700 %{buildroot}/etc/sysSentry/tasks/
install -d -m 700 %{buildroot}/etc/sysSentry/plugins/
install -m 600 config/inspect.conf %{buildroot}%{_sysconfdir}/sysSentry
install -m 600 service/sysSentry.service %{buildroot}%{_unitdir}

# xalarm
sh build/build.sh -i %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 600 config/xalarm.conf %{buildroot}%{_sysconfdir}/sysSentry
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/xalarm
install -m 600 service/xalarmd.service %{buildroot}%{_unitdir}
install -m 600 config/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/sysSentry
install -m 644 src/libso/xalarm/register_xalarm.h %{buildroot}%{_includedir}/xalarm/register_xalarm.h

# cpu sentry
install config/tasks/cpu_sentry.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/cpu_sentry.ini %{buildroot}/etc/sysSentry/plugins/cpu_sentry.ini
install src/c/catcli/catlib/build/cat-cli %{buildroot}%{_bindir}/cat-cli
install src/c/catcli/catlib/build/plugin/cpu_patrol/libcpu_patrol.so %{buildroot}%{_libdir}

chrpath -d %{buildroot}%{_bindir}/cat-cli
chrpath -d %{buildroot}%{_libdir}/libcpu_patrol.so

pushd src/python
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=SENTRY_FILES
popd

%pre

%post
/sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
    systemctl stop xalarmd.service
    systemctl disable xalarmd.service
    systemctl stop sysSentry.service
    systemctl disable sysSentry.service
fi
rm -rf /var/run/xalarm | :
rm -rf /var/run/sysSentry | :

%postun
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -f src/python/SENTRY_FILES
%defattr(0550,root,root)
%attr(0550,root,root) %{python3_sitelib}/xalarm
%attr(0550,root,root) %{python3_sitelib}/syssentry

# sysSentry
%attr(0500,root,root) %{_bindir}/sentryctl
%attr(0550,root,root) %{_bindir}/syssentry
%attr(0750,root,root) %config(noreplace) %{_var}/log/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/plugins
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/inspect.conf
%attr(0600,root,root) %{_unitdir}/sysSentry.service

# xalarm
%attr(0550,root,root) %{_bindir}/xalarmd
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/sysSentry
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/xalarm.conf
%attr(0600,root,root) %{_unitdir}/xalarmd.service

# cpu inspection module
%exclude %{_sysconfdir}/sysSentry/tasks/cpu_sentry.mod
%exclude %{_sysconfdir}/sysSentry/plugins/cpu_sentry.ini
%exclude %{_bindir}/cpu_sentry
%exclude %{_bindir}/cat-cli
%exclude %{python3_sitelib}/syssentry/cpu_*
%exclude %{python3_sitelib}/syssentry/*/cpu_*

%files -n libxalarm
%attr(0550,root,root) %{_libdir}/libxalarm.so

%files -n libxalarm-devel
%dir %{_includedir}/xalarm
%attr(0550,root,root) %{_includedir}/xalarm
%attr(0550,root,root) %{_includedir}/xalarm/register_xalarm.h

%files -n cpu_sentry
%attr(0500,root,root) %{_bindir}/cat-cli
%attr(0500,root,root) %{_bindir}/cpu_sentry
%attr(0550,root,root) %{_libdir}/libcpu_patrol.so
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/cpu_sentry.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/cpu_sentry.ini
%attr(0550,root,root) %{python3_sitelib}/syssentry/cpu_*

%changelog
* Mon Sep 09 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-10
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:split cpu_sentry and syssentry

* Mon Sep 02 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-9
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:Remove ANSI escape sequences

* Sat Aug 31 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-8
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add ipmitool to Recommends for cpu_sentry

* Sat Aug 31 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-7
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add deleted code to plugin rasdaemon

* Fri Aug 30 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-6
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:setting parameters must be integer

* Wed Aug 28 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-5
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:cpu_utility and cpu_patrol must be an integer

* Fri Jul 26 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-4
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix result when process output is None

* Thu Jul 25 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-3
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:Fix the problem that function cpu_report_result() is called more than once
       fix error handling

* Tue Jun 18 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-2
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:delete rpath setting

* Tue Jun 11 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-1
- Type:enhancement
- CVE:NA
- SUG:NA
- DESC:Package init
