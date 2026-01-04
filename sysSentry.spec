# Copyright (c) Huawei Technologies Co., Ltd. 2014-2023. All rights reserved.
# Description: spec file for package syssentry

Summary: System Inspection Framework
Name: sysSentry
Version: 1.0.3
Release: 21
License: Mulan PSL v2
Group: System Environment/Daemons
Source0: https://gitee.com/openeuler/sysSentry/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch1:    add-bidirectional-communication-for-xalarm.patch
Patch2:    fix-some-test-cases.patch
Patch3:    add-log-for-xalarmd-and-fix-delete-on-iter-problem.patch
Patch4:    fix-xalarm-log-not-print-and-add-on-iter-problem.patch
Patch5:    add-new-func-for-ebpf-in-the-rq_driver-stage.patch
Patch6:    fix-the-sentryCollector-service-can-t-be-stopped-for.patch
Patch7:    ai-block-io-exit-when-stage-is-not-supported.patch
Patch8:    add-log-utils-for-c.patch
Patch9:    fix-env-for-subprocess.Popen.patch
Patch10:   fix-period-task-some-bugs.patch
Patch11:   Add-SOC-Ring-sentry-function.patch
Patch12:   Add-testcase-tc_ring-for-SOC-Ring-sentry.patch
Patch13:   testcase-tc_ring-cleancode.patch
Patch14:   Fix-issue-cores-with-isolcpus-set-blacklis.patch
Patch15:   Fix-issue-inconsistent-status-and-result-a.patch
Patch16:   Use-panic-instead-of-coredump-file.patch
Patch17:   Fix-Security-Scan-Warning.patch
Patch18:   Fix-two-code-review-comments.patch
Patch19:   Add-MulanV2-License-statement.patch
Patch20:   add-bmc_block_io-and-slow-io-plugin-upgrade.patch
Patch21:   add-disk-latency-collect.patch
Patch22:   add-dfx-for-xalarmd-to-rebuild-connection-after-comm.patch
Patch23:   fix-an-issue-with-printing-error.patch
Patch24:   add-sentry-msg-monitor.patch
Patch25:   add-oom-event-report.patch
Patch26:   Use-malloc-to-allocate-memory-as-much-as-possible.patch
Patch27:   fix-xalarmd-stop-failed-by-systemd.patch
Patch28:   fix-systemctl-stop-error-bug-that-clientId-is-a-loca.patch
Patch29:   fix-missing-pycache-file.patch
Patch30:   fix-python-files-permission.patch
Patch31:   fix-sys-exit-bug.patch
Patch32:   fix-some-warnings.patch
Patch33:   fix-log_utils.patch
Patch34:   fix-error-code-for-socket-failed.patch
Patch35:   fix-typo.patch
Patch36:   Fix-resource-leak.patch
Patch37:   fix-buffer-overflow-in-checkset_cpulist.patch
Patch38:   Fix-the-use-of-uninitialized-variable-ret.patch
Patch39:   report-panic-and-kernel-reboot-event.patch
Patch40:   add-NONZERO_EXITED-status-for-plugin-exited-with-non.patch
Patch41:   fix-process-exit-status-and-service-kill-mode.patch
Patch42:   add-UB-fault-report-function.patch
Patch43:   support-to-send-SIGBUS-signal-for-UB-memory-fault.patch
Patch44:   fix-resource-leak-in-hbm_online_repair.patch
Patch45:   fix-Out-of-memory-bounds-access-in-ebpf_collector.patch
Patch46:   report-power-off-result-to-BMC.patch
Patch47:   add-API-to-enable-disable-the-hijacking-function-for.patch
Patch48:   build-sentry_msg_monitor-only-under-aarch64-architec.patch
Patch49:   fix-syntar-in-sentryctl.patch
Patch50:   add-task_pre-and-task_post-for-task-mod-setting.patch
Patch51:   fix-potential-use-after-free-bugs-in-libxalarm.patch
Patch52:   change-egg-info-dir-permission.patch
Patch53:   keeping-the-driver-loaded-in-the-reboot-scenario.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3 python3-setuptools
BuildRequires: json-c-devel
BuildRequires: chrpath
BuildRequires: elfutils-devel clang libbpf-devel bpftool
BuildRequires: python3-numpy python3-pytest
BuildRequires: numactl-libs numactl-devel

Requires:      pyxalarm = %{version}
Requires:      libbpf nvme-cli

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

%ifarch aarch64
%package -n sentry_msg_monitor
Summary:        A plugin for sysSentry to listening specific messages
Requires:       sysSentry = %{version}-%{release}
Provides:       sentry_msg_monitor = %{version}
BuildRequires:  libobmm-devel
Requires:       lsof libobmm ipmitool

%description -n sentry_msg_monitor
This package provides a plugin for sysSentry to listening specific messages
%endif

%package -n bmc_block_io
Summary:        bmc_block_io for the sysSentry
Provides:       bmc_block_io = %{version}
BuildRequires:  json-c-devel
Requires:       libxalarm ipmitool json-c
Requires:       sysSentry = %{version}-%{release}

%description -n bmc_block_io
This package provides bmc_block_io for the sysSentry.

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
%attr(0555,root,root) %{python3_sitelib}/xalarm
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
%exclude %{_sysconfdir}/sysSentry/tasks/bmc_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/bmc_block_io.ini

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
%attr(0550,root,root) %{_libdir}/libsentry_log.so

%exclude %{_includedir}/libsentry/log_utils.h
%exclude %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%exclude %{python3_sitelib}/syssentry/bmc_*
%exclude %{python3_sitelib}/syssentry/*/bmc_*

# soc_ring_sentry
%exclude %{_sysconfdir}/sysconfig/soc_ring_sentry.env
%exclude %{_sysconfdir}/sysSentry/tasks/soc_ring_sentry.mod

# sentry_msg_monitor
%exclude %{_sysconfdir}/sysconfig/sentry_msg_monitor.env
%exclude %{_sysconfdir}/sysSentry/tasks/sentry_msg_monitor.mod
%exclude %{_sysconfdir}/sysSentry/task_scripts/sentry_msg_monitor.sh

%files -n libxalarm
%attr(0555,root,root) %{_libdir}/libxalarm.so

%files -n libxalarm-devel
%attr(0555,root,root) %{_includedir}/xalarm/register_xalarm.h

%files -n pyxalarm
%attr(0555,root,root) %{python3_sitelib}/xalarm/register_xalarm.py

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

%ifarch aarch64
%files -n sentry_msg_monitor
%attr(0550,root,root) %{_bindir}/sentry_msg_monitor
%attr(0600,root,root) %{_sysconfdir}/sysconfig/sentry_msg_monitor.env
%attr(0600,root,root) %{_sysconfdir}/sysSentry/tasks/sentry_msg_monitor.mod
%attr(0600,root,root) %{_sysconfdir}/sysSentry/task_scripts/sentry_msg_monitor.sh
%endif

%files -n bmc_block_io
%attr(0550,root,root) %{_bindir}/bmc_block_io
%attr(0600,root,root) %{_sysconfdir}/sysSentry/plugins/bmc_block_io.ini
%attr(0600,root,root) %{_sysconfdir}/sysSentry/tasks/bmc_block_io.mod

%files -n soc_ring_sentry
%attr(0750,root,root) %{_bindir}/soc_ring_sentry
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/soc_ring_sentry.env
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/soc_ring_sentry.mod

%changelog
* Mon Dec 29 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-21
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:keeping the driver loaded in the reboot scenario

* Wed Dec 10 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-20
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: change egg-info dir permission

* Tue Dec 09 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-19
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix potential use-after-free bugs in libxalarm

* Wed Dec 03 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-18
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add task_pre and task_post for task mod setting

* Wed Dec 03 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-17
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:Fix self-dependency issue in spec file

* Fri Nov 28 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-16
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix syntar in sentryctl

* Thu Nov 27 2025 shixuantong <shixuantong1@h-partners.com> - 1.0.3-15
- Type:feature
- CVE:NA
- SUG:NA
- DESC:add sentry msg monitor
       support oom/power off/ub mem fault/panic/reboot event hijackin

* Mon Nov 17 2025 hewanhan <hewanhan@h-partners.com> - 1.0.3-14
- Type:feature
- CVE:NA
- SUG:NA
- DESC:add disk latency collect

* Tue Nov 4 2025 hewanhan <hewanhan@h-partners.com> - 1.0.3-13
- Type:feature
- CVE:NA
- SUG:NA
- DESC:add bmc_block_io and slow io plugin upgrade

* Tue Oct 21 2025 Qizhi Zhang <zhangqizhi3@h-partners.com> - 1.0.3-12
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Fix the syssentry.spec file that was incorrectly field out by soc_ring_sentry

* Fri Oct 17 2025 Qizhi Zhang <zhangqizhi3@h-partners.com> - 1.0.3-11
- Type:feature
- CVE:NA
- SUG:NA
- DESC:Add SOC Ring sentry function
       Add testcase tc_ring for SOC Ring sentry
       testcase tc_ring cleancode
       Fix issue cores with isolcpus set blacklist failed
       Fix issue inconsistent status and result after single inspection
       Use panic instead of coredump file
       Fix Security Scan Warning
       Fix two code review comments
       Add MulanV2 License statement

* Sat Mar 29 2025 shixuantong <shixuantong1@huawei.com> - 1.0.3-10
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix period task some bugs
       fix env_file and environ_conf

* Fri Mar 14 2025 shixuantong <shixuantong1@huawei.com> - 1.0.3-9
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add log utils for c

* Thu Mar 13 2025 luckky <guodashun1@huawei.com> - 1.0.3-8
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: fix an issue with printing error

* Mon Feb 24 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.3-7
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: fix the sentryCollector service can't be stopped for a long

* Sat Feb 22 2025 zhuofeng <zhuofeng2@huawei.com> - 1.0.3-6
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: add new func for ebpf in the rq_driver stage

* Tue Feb 18 2025 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.3-5
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: fix xalarm log not print and add on iter problem

* Tue Feb 18 2025 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.3-4
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC: add log for xalarmd and fix delete on iter problem

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
