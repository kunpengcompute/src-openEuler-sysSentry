# Copyright (c) Huawei Technologies Co., Ltd. 2014-2023. All rights reserved.
# Description: spec file for package syssentry

Summary: System Inspection Framework
Name: sysSentry
Version: 1.0.3
Release: 3
License: Mulan PSL v2
Group: System Environment/Daemons
Source0: https://gitee.com/openeuler/sysSentry/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch1:    add-bidirectional-communication-for-xalarm.patch
Patch2:    fix-some-test-cases.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3 python3-setuptools
BuildRequires: json-c-devel
BuildRequires: chrpath
BuildRequires: elfutils-devel clang libbpf-devel bpftool
BuildRequires: python3-numpy python3-pytest

Requires:      pyxalarm = %{version}
Requires:      libbpf

%define PYTHON_VERSION %{python3_version}
%define PKGVER syssentry-%{version}-py%{PYTHON_VERSION}.egg-info

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

%package -n avg_block_io
Summary:        Supports slow I/O detection
Requires:       sysSentry = %{version}-%{release}
Requires:       pysentry_notify = %{version}-%{release}
Requires:       pysentry_collect = %{version}-%{release}

%description -n avg_block_io
This package provides Supports slow I/O detection based on EBPF

%package -n ai_block_io
Summary:        Supports slow I/O detection
Requires:       python3-numpy
Requires:       sysSentry = %{version}-%{release}
Requires:       pysentry_notify = %{version}-%{release}
Requires:       pysentry_collect = %{version}-%{release}

%description -n ai_block_io
This package provides Supports slow I/O detection based on AI

%package -n pyxalarm
Summary:        Supports xalarm api in python immplementation
Requires:       sysSentry = %{version}-%{release}

%description -n pyxalarm
This package provides Supports xalarm api for users

%package -n pysentry_notify
Summary:        Supports xalarm report in python immplementation
Requires:       sysSentry = %{version}-%{release}

%description -n pysentry_notify
This package provides Supports xalarm report for plugins

%package -n pysentry_collect
Summary:        Supports collect in python immplementation
Requires:       sysSentry = %{version}-%{release}

%description -n pysentry_collect
This package provides Supports collect for plugins

%package -n hbm_online_repair
Summary:        hbm_online_repair for the sysSentry
Provides:       hbm_online_repair = %{version}
BuildRequires:  libtraceevent-devel
Requires:       libtraceevent ipmitool
Requires:       sysSentry = %{version}-%{release}

%description -n hbm_online_repair
This package provides hbm_online_repair for the sysSentry.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build

%install
%make_install

%post
/sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
    systemctl stop xalarmd.service
    systemctl disable xalarmd.service
    systemctl stop sysSentry.service
    systemctl disable sysSentry.service
    systemctl stop sentryCollector.service
    systemctl disable sentryCollector.service
fi
rm -rf /var/run/xalarm | :
rm -rf /var/run/sysSentry | :

%postun
/sbin/ldconfig

%files
%defattr(0550,root,root)
%attr(0550,root,root) %{python3_sitelib}/xalarm
%attr(0550,root,root) %{python3_sitelib}/syssentry
%attr(0550,root,root) %{python3_sitelib}/%{PKGVER}
%attr(0550,root,root) %{python3_sitelib}/sentryCollector

# sysSentry
%attr(0500,root,root) %{_bindir}/sentryctl
%attr(0550,root,root) %{_bindir}/syssentry
%attr(0550,root,root) %{_bindir}/ebpf_collector
%attr(0750,root,root) %config(noreplace) %{_var}/log/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/plugins
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/inspect.conf
%attr(0600,root,root) %{_unitdir}/sysSentry.service

%exclude %{python3_sitelib}/sentryCollector/collect_plugin.py
%exclude %{python3_sitelib}/xalarm/register_xalarm.py
%exclude %{python3_sitelib}/xalarm/sentry_notify.py

%exclude %{python3_sitelib}/syssentry/__pycache__
%exclude %{python3_sitelib}/sentryCollector/__pycache__
%exclude %{python3_sitelib}/xalarm/__pycache__

%exclude %{_sysconfdir}/sysSentry/tasks/ai_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/ai_block_io.ini
%exclude %{_sysconfdir}/sysSentry/tasks/avg_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/avg_block_io.ini

# xalarm
%attr(0550,root,root) %{_bindir}/xalarmd
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/xalarm.conf
%attr(0600,root,root) %{_unitdir}/xalarmd.service

# logrotate
%dir %{_localstatedir}/lib/logrotate-syssentry
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/logrotate-sysSentry.conf
%attr(0500,root,root) %{_sysconfdir}/cron.hourly/logrotate-sysSentry

# sentryCollector
%attr(0550,root,root) %{_bindir}/sentryCollector
%attr(0600,root,root) %{_sysconfdir}/sysSentry/collector.conf
%attr(0600,root,root) %{_unitdir}/sentryCollector.service

%exclude %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%exclude %{python3_sitelib}/syssentry/bmc_*
%exclude %{python3_sitelib}/syssentry/*/bmc_*

%files -n libxalarm
%attr(0550,root,root) %{_libdir}/libxalarm.so

%files -n libxalarm-devel
%attr(0550,root,root) %{_includedir}/xalarm/register_xalarm.h

%files -n pyxalarm
%attr(0550,root,root) %{python3_sitelib}/xalarm/register_xalarm.py

%files -n pysentry_notify
%attr(0550,root,root) %{python3_sitelib}/xalarm/sentry_notify.py

%files -n avg_block_io
%attr(0500,root,root) %{_bindir}/avg_block_io
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/avg_block_io.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/avg_block_io.ini
%attr(0550,root,root) %{python3_sitelib}/sentryPlugins/avg_block_io
%exclude %{python3_sitelib}/sentryPlugins/avg_block_io/__pycache__

%files -n ai_block_io
%attr(0500,root,root) %{_bindir}/ai_block_io
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/ai_block_io.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/ai_block_io.ini
%attr(0550,root,root) %{python3_sitelib}/sentryPlugins/ai_block_io
%exclude %{python3_sitelib}/sentryPlugins/ai_block_io/__pycache__

%files -n pysentry_collect
%attr(0550,root,root) %{python3_sitelib}/sentryCollector/collect_plugin.py

%files -n hbm_online_repair
%attr(0550,root,root) %{_bindir}/hbm_online_repair
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/hbm_online_repair.env
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%attr(0550,root,root) %{python3_sitelib}/syssentry/bmc_alarm.py

%changelog
* Fri Feb 14 2025 jinsaihang <jinsaihang@h-partners.com> - 1.0.3-3
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: fix some test cases

* Sat Feb 8 2025 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.3-2
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: add bidirectional communication for libxalarm

* Mon Jan 20 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.3-1
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:1.0.3 init
