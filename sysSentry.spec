# Copyright (c) Huawei Technologies Co., Ltd. 2014-2023. All rights reserved.
# Description: spec file for package syssentry

Summary: System Inspection Framework
Name: sysSentry
Version: 1.0.2
Release: 40
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
Patch11:   fix-configparser.InterpolationSyntaxError.patch
Patch12:   fix-syssentry-fails-to-be-started-when-cpu_sentry-is.patch
Patch13:   optimize-the-handing-of-cat-cli-error-msg-in-cpu_sentry.patch
Patch14:   over-threshold-should-be-warn-level-log-in-cat-cli.patch
Patch15:   add-separator-to-err-info.patch
Patch16:   remove-threshold-max-cpu-cores.patch
Patch17:   add-hbm-online-repair.patch
Patch18:   fix-hbm-online-repair-notice-and-efi-create.patch
Patch19:   fix-uint8-bug-and-change-isolation-default-value.patch
Patch20:   fix-write-file-return-code-bug.patch
Patch21:   update-the-commit-of-the-log-level-and-format-of-sys.patch
Patch22:   add-boundary-check-for-settings.patch
Patch23:   fix-xalarm-not-reject-alarm-msg-exceeds-max-length.patch
Patch24:   change-status-of-period-task-and-sort-mod-file.patch
Patch25:   set-logrotate.patch
Patch26:   hbm_online_repair-add-unload-driver.patch
Patch27:   add-pyxalarm-and-pySentryNotify-add-multi-users-supp.patch
Patch28:   adapt_5.10_kenel_for_syssentry.patch
Patch29:   collect-module-adapt-to-the-5.10-kernel.patch
Patch30:   add-avg_block_io-and-ai_block_io.patch
Patch31:   fix-bug-of-ebpf-and-ai_block_io.patch
Patch32:   fix-the-sentryCollector-service-can-t-be-stopped-for.patch
Patch33:   ai-block-io-exit-when-stage-is-not-supported.patch
Patch34:   fix-period-task-some-bugs.patch
Patch35:   fix-env_file-and-environ_conf.patch
Patch36:   fix-cpu_sentry-result-when-found_fault_cores_number-.patch
Patch37:   add-huge-page-aggregation.patch
Patch38:   add-soc_ring_sentry-plugin.patch
Patch39:   fix-the-potential-KeyError-exception-in-task_get_ala.patch
Patch40:   fix-potential-crash-issue-in-bmc_recv.patch
Patch41:   add-NONZERO_EXITED-status-for-plugin-exited-with-non.patch
Patch42:   fix-process-exit-status-and-service-kill-mode.patch
Patch43:   fix-period-type-task-abnormal-status.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3 python3-setuptools
BuildRequires: json-c-devel
BuildRequires: chrpath
BuildRequires: elfutils-devel clang libbpf-devel bpftool
BuildRequires: python3-numpy python3-pytest
Requires:      libxalarm = %{version}
Requires:      libbpf

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

%package -n cpu_sentry
Summary:        CPU fault inspection program
Requires:       procps-ng
Recommends:     sysSentry = %{version}-%{release}
Recommends:     ipmitool

%description -n cpu_sentry
This package provides CPU fault detection

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

%package -n soc_ring_sentry
Summary:        soc_ring_sentry for the sysSentry
Provides:       soc_ring_sentry = %{version}
BuildRequires:  numactl-libs numactl-devel
Requires:       sysSentry = %{version}-%{release}

%description -n soc_ring_sentry
This package provides soc_ring_sentry for the sysSentry.

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

# hbm_online_repair
pushd src/c/hbm_online_repair
make
popd

# log
pushd src/libso/log
cmake . -B build
pushd build
make
popd
popd

# soc_ring_sentry
pushd src/c/soc_ring_sentry
make
popd

pushd src/c/ebpf_collector
make
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
install -m 755 src/c/ebpf_collector/ebpf_collector %{buildroot}%{_bindir}

# rasdaemon
install config/tasks/rasdaemon.mod %{buildroot}/etc/sysSentry/tasks/

# xalarm
sh build/build.sh -i %{buildroot}%{_libdir}
install -m 600 config/xalarm.conf %{buildroot}%{_sysconfdir}/sysSentry
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/xalarm
install -m 600 service/xalarmd.service %{buildroot}%{_unitdir}
install -m 644 src/libso/xalarm/register_xalarm.h %{buildroot}%{_includedir}/xalarm/register_xalarm.h

# sentryCollector
install -m 600 config/collector.conf %{buildroot}%{_sysconfdir}/sysSentry
install -m 600 service/sentryCollector.service %{buildroot}%{_unitdir}

# cpu sentry
install config/tasks/cpu_sentry.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/cpu_sentry.ini %{buildroot}/etc/sysSentry/plugins/cpu_sentry.ini
install src/c/catcli/catlib/build/cat-cli %{buildroot}%{_bindir}/cat-cli
install src/c/catcli/catlib/build/plugin/cpu_patrol/libcpu_patrol.so %{buildroot}%{_libdir}

# hbm_online_repair
mkdir -p %{buildroot}/etc/sysconfig/
install config/tasks/hbm_online_repair.mod %{buildroot}/etc/sysSentry/tasks/
install src/c/hbm_online_repair/hbm_online_repair %{buildroot}%{_bindir}
install src/c/hbm_online_repair/hbm_online_repair.env %{buildroot}/etc/sysconfig/hbm_online_repair.env

# soc_ring_sentry
install	src/c/soc_ring_sentry/soc_ring_sentry %{buildroot}%{_bindir}
install config/env/soc_ring_sentry.env %{buildroot}/etc/sysconfig/soc_ring_sentry.env
install config/tasks/soc_ring_sentry.mod %{buildroot}/etc/sysSentry/tasks/
install src/libso/log/build/libsentry_log.so %{buildroot}%{_libdir}

chrpath -d %{buildroot}%{_bindir}/cat-cli
chrpath -d %{buildroot}%{_libdir}/libcpu_patrol.so

# avg_block_io
install config/tasks/avg_block_io.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/avg_block_io.ini %{buildroot}/etc/sysSentry/plugins/avg_block_io.ini

# ai_block_io
install config/tasks/ai_block_io.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/ai_block_io.ini %{buildroot}/etc/sysSentry/plugins/ai_block_io.ini

# logrotate
mkdir -p %{buildroot}%{_localstatedir}/lib/logrotate-syssentry
mkdir -p %{buildroot}%{_sysconfdir}/cron.hourly
install -m 0600 config/logrotate-sysSentry.conf %{buildroot}%{_sysconfdir}/sysSentry/logrotate-sysSentry.conf
install -m 0500 src/sh/logrotate-sysSentry.cron %{buildroot}%{_sysconfdir}/cron.hourly/logrotate-sysSentry

pushd src/python
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=SENTRY_FILES
cat SENTRY_FILES | grep -v register_xalarm.* | grep -v sentry_notify.*  > SENTRY_FILES.tmp
mv SENTRY_FILES.tmp SENTRY_FILES
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
    systemctl stop sentryCollector.service
    systemctl disable sentryCollector.service
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
%attr(0550,root,root) %{python3_sitelib}/sentryCollector

# sysSentry
%attr(0500,root,root) %{_bindir}/sentryctl
%attr(0550,root,root) %{_bindir}/syssentry
%attr(0750,root,root) %config(noreplace) %{_var}/log/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/plugins
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/inspect.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/rasdaemon.mod
%attr(0600,root,root) %{_unitdir}/sysSentry.service
%attr(0755,root,root) %{_bindir}/ebpf_collector

# xalarm
%attr(0550,root,root) %{_bindir}/xalarmd
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/xalarm.conf
%attr(0600,root,root) %{_unitdir}/xalarmd.service

# avg block io
%exclude %{_sysconfdir}/sysSentry/tasks/avg_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/avg_block_io.ini
%exclude %{_bindir}/avg_block_io
%exclude %{python3_sitelib}/sentryPlugins/*

# ai_block_io
%exclude %{_sysconfdir}/sysSentry/tasks/ai_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/ai_block_io.ini
%exclude %{_bindir}/ai_block_io
%exclude %{python3_sitelib}/sentryPlugins/*

# sentryCollector
%attr(0550,root,root) %{_bindir}/sentryCollector
%attr(0600,root,root) %{_sysconfdir}/sysSentry/collector.conf
%attr(0600,root,root) %{_unitdir}/sentryCollector.service
%attr(0550,root,root) %{_libdir}/libsentry_log.so

# pysentry_collect
%exclude %{python3_sitelib}/sentryCollector/collect_plugin.py
%exclude %{python3_sitelib}/sentryCollector/__pycache__/collect_plugin*

# logrotate
%dir %{_localstatedir}/lib/logrotate-syssentry
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/logrotate-sysSentry.conf
%attr(0500,root,root) %{_sysconfdir}/cron.hourly/logrotate-sysSentry

# cpu inspection module
%exclude %{_sysconfdir}/sysSentry/tasks/cpu_sentry.mod
%exclude %{_sysconfdir}/sysSentry/plugins/cpu_sentry.ini
%exclude %{_bindir}/cpu_sentry
%exclude %{_bindir}/cat-cli
%exclude %{python3_sitelib}/syssentry/cpu_*
%exclude %{python3_sitelib}/syssentry/*/cpu_*

# hbm repair module
%exclude %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%exclude %{python3_sitelib}/syssentry/bmc_*
%exclude %{python3_sitelib}/syssentry/*/bmc_*

# soc_ring_sentry
%exclude %{_sysconfdir}/sysconfig/soc_ring_sentry.env
%exclude %{_sysconfdir}/sysSentry/tasks/soc_ring_sentry.mod

%files -n avg_block_io
%attr(0500,root,root) %{_bindir}/avg_block_io
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/avg_block_io.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/avg_block_io.ini
%attr(0550,root,root) %{python3_sitelib}/sentryPlugins/avg_block_io

%files -n ai_block_io
%attr(0500,root,root) %{_bindir}/ai_block_io
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/ai_block_io.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/ai_block_io.ini
%attr(0550,root,root) %{python3_sitelib}/sentryPlugins/ai_block_io

# hbm repair module
%exclude %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%exclude %{python3_sitelib}/syssentry/bmc_*
%exclude %{python3_sitelib}/syssentry/*/bmc_*

%files -n libxalarm
%attr(0550,root,root) %{_libdir}/libxalarm.so

%files -n libxalarm-devel
%dir %{_includedir}/xalarm
%attr(0550,root,root) %{_includedir}/xalarm
%attr(0550,root,root) %{_includedir}/xalarm/register_xalarm.h

%files -n pyxalarm
%attr(0550,root,root) %{python3_sitelib}/xalarm/register_xalarm.py
%attr(0550,root,root) %{python3_sitelib}/xalarm/__pycache__/register_xalarm*

%files -n pysentry_notify
%attr(0550,root,root) %{python3_sitelib}/xalarm/sentry_notify.py
%attr(0550,root,root) %{python3_sitelib}/xalarm/__pycache__/sentry_notify*

%files -n cpu_sentry
%attr(0500,root,root) %{_bindir}/cat-cli
%attr(0500,root,root) %{_bindir}/cpu_sentry
%attr(0550,root,root) %{_libdir}/libcpu_patrol.so
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/cpu_sentry.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/cpu_sentry.ini
%attr(0550,root,root) %{python3_sitelib}/syssentry/cpu_*

%files -n hbm_online_repair
%attr(0550,root,root) %{_bindir}/hbm_online_repair
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/hbm_online_repair.env
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%attr(0550,root,root) %{python3_sitelib}/syssentry/bmc_alarm.py

%files -n pysentry_collect
%attr(0550,root,root) %{python3_sitelib}/sentryCollector/collect_plugin.py
%attr(0550,root,root) %{python3_sitelib}/sentryCollector/__pycache__/collect_plugin*

%files -n soc_ring_sentry
%attr(0550,root,root) %{_bindir}/soc_ring_sentry
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/soc_ring_sentry.env
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/soc_ring_sentry.mod

%changelog
* Sat Feb 07 2026 shixuantong <shixuantong1@h-partners.com> - 1.0.2-40
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix period type task abnormal status

* Thu Jan 29 2026 shixuantong <shixuantong1@h-partners.com> - 1.0.2-39
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add NONZERO_EXITED status for plugin exited with non-zero
       fix process exit status and service kill mode

* Fri Jan 23 2026 shixuantong <shixuantong1@h-partners.com> - 1.0.2-38
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:some bugfix

* Fri Jan 9 2026 zengchao001 <zc18179036325@163.com> - 1.0.2-37
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add soc_ring_sentry plugin

* Tue Sep 09 2025 zhuo <1107893276@qq.com> - 1.0.2-36
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add huge page aggregation

* Sat May 17 2025 shixuantong <shixuantong1@huawei.com> - 1.0.2-35
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix cpu_sentry result when found_fault_cores_number != isolated_cores_number

* Sat Mar 29 2025 shixuantong <shixuantong1@huawei.com> - 1.0.2-34
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix period task some bugs
       fix env_file and environ_conf

* Thu Mar 13 2025 luckky <guodashun1@huawei.com> - 1.0.2-33
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: fix an issue with printing error

* Thu Mar 13 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-32
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix the sentryCollector service can't be stopped for a long

* Fri Feb 14 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-31
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix bug of ebpf and ai_block_io

* Sun Jan 26 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-30
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add avg_block_io and ai_block_io

* Sun Jan 26 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-29
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:collect module adapt to the 5.10 kernel

* Fri Jan 24 2025 jinsaihang <jinsaihang@h-partners.com> - 1.0.2-28
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:adapt get_alarm for kenel 5.10

* Wed Jan 22 2025 shixuantong <shixuantong@huawei.com> - 1.0.2-27
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:move logrotate-sysSentry.conf from /etc/ to /etc/sysSentry/

* Fri Jan 17 2025 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-26
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: add multi user support for xalarm, pyxalarm and pySentryNotify

* Wed Dec 18 2024 luckky <guodashun1@huawei.com> - 1.0.2-25
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: add boundary check for settings

* Wed Dec 18 2024 shixuantong <shixuantong@huawei.com> - 1.0.2-24
- Type:enhancement
- CVE:NA
- SUG:NA
- DESC:set logrotate

* Fri Dec 13 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-23
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: change status of period task and sort mod file

* Thu Nov 7 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-22
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: fix xalarm not reject alarm msg exceeds max length

* Wed Nov 6 2024 luckky <guodashun1@huawei.com> - 1.0.2-21
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: add boundary check for settings

* Tue Nov 5 2024 luckky <guodashun1@huawei.com> - 1.0.2-20
- Type:enhancement
- CVE:NA
- SUG:NA
- DESC: update the commit of the log level and format function of sysSentry

* Mon Nov 4 2024 luckky <guodashun1@huawei.com> - 1.0.2-19
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix write file return code bug

* Fri Nov 1 2024 luckky <guodashun1@huawei.com> - 1.0.2-18
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix uint8 bug and change page isolation threshold default value

* Mon Oct 28 2024 luckky <guodashun1@huawei.com> - 1.0.2-17
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix hbm_online_repair notice BMC function and create efi fd

* Mon Oct 21 2024 luckky <guodashun1@huawei.com> - 1.0.2-16
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add hbm_online_repair

* Wed Sep 25 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-15
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove threshold:max cpu cores

* Wed Sep 25 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-14
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add separator to err info

* Sat Sep 21 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-13
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:optimize the handing of cat-cli error msg in cpu_sentry
       over threshold should be warn level log in cat-cli

* Sat Sep 14 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-12
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix syssentry fails to be started when cpu_sentry is not installed

* Wed Sep 11 2024 shixuantong <shixuantong1@huawei.com> - 1.0.2-11
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix configparser.InterpolationSyntaxError

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
