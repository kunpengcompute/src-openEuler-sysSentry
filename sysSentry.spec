# Copyright (c) Huawei Technologies Co., Ltd. 2014-2023. All rights reserved.
# Description: spec file for package syssentry

Summary: System Inspection Framework
Name: sysSentry
Version: 1.0.2
Release: 54
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
Patch13:   add-collect-module-to-sysSentry.patch
Patch14:   feature-add-avg_block_io-plugin.patch
Patch15:   fix-some-about-collect-module-and-avg-block-io.patch
Patch16:   add-ai-threshold-slow-io-detection-plugin.patch
Patch17:   fix-bug-step-2-about-collect-module-and-avg-block-io.patch
Patch18:   add-log-level-and-change-log-format.patch
Patch19:   fix-ai_block_io-some-issues.patch
Patch20:   add-ebpf-collector.patch
Patch21:   add-pyxalarm-and-pySentryNotify-add-multi-users-supp.patch
Patch22:   add-sentryctl-get_alarm-module_name-s-time_range-d.patch
Patch23:   fix-python-3.7-not-support-list-bool-type.patch
Patch24:   avg_block_io-send-alarm-to-xalarmd.patch
Patch25:   update-log-when-it-is-not-lock-collect.patch
Patch26:   ebpf-update-log.patch
Patch27:   change-alarm-length.patch
Patch28:   add-detail-time.patch
Patch29:   fix-config-relative-some-issues.patch
Patch30:   ebpf-fix-alarm-bug.patch
Patch31:   xalarm-add-alarm-msg-length-to-8192.patch
Patch32:   add-log-for-improving-maintainability.patch
Patch33:   add-get_disk_type-and-fix-some-bugs.patch
Patch34:   ai_block_io-adapt-alarm-module.patch
Patch35:   diff-disk-type-use-diff-config.patch
Patch36:   add-parameter-time_range-alarm_id-and-alarm_clear_ti.patch
Patch37:   fix-xalarm_Report-function-not-refuse-alarm-msg-exce.patch
Patch38:   fix-xalarm_upgrade-not-return-val-and-fail-when-thre.patch
Patch39:   add-log-for-xalarm-when-sending-msg-and-clean-invali.patch
Patch40:   add-xalarm-cleanup-invalid-server-socket-peroidly.patch
Patch41:   ai_block_io-support-stage-and-iotype.patch
Patch42:   ebpf-fix-collect-iodump.patch
Patch43:   fix-io_dump-for-collect-module.patch
Patch44:   add-root-cause-analysis.patch
Patch45:   update-collect-log.patch
Patch46:   modify-abnormal-stack-when-the-disk-field-is-not-con.patch
Patch47:   precise-alarm-query-time.patch
Patch48:   ebpf-fix-dead-loop.patch
Patch49:   fix-word-error.patch
Patch50:   ai_block_io-fix-some-bugs.patch
Patch51:   refactor-config.py-and-bugfix-uncorrect-slow-io-repo.patch
Patch52:   get_io_data-failed-wont-stop-avg_block_io-and-del-di.patch
Patch53:   listen-thread-of-collect-module-exits-occasionally.patch
Patch54:   fix-ai_block_io-root-cause-bug.patch
Patch55:   ebpf-fix-kyqin-miss-rq_driver-data.patch
Patch56:   optimize-log-printing.patch
Patch57:   enrich-alert-info-about-kernel-stack.patch
Patch58:   ebpf-fix-iodump-warning.patch
Patch59:   ai_block_io-lack-section-exit.patch
Patch60:   fix-xalarm-non-uniform-log-formatting.patch 
Patch61:   update-collect-plugin-period-max.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3 python3-setuptools
BuildRequires: json-c-devel
BuildRequires: chrpath
BuildRequires: elfutils-devel clang libbpf-devel llvm kernel-source
Requires:      libxalarm = %{version}
Requires:      libbpf
Requires:      pyxalarm = %{version}

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
install -m 700 src/c/ebpf_collector/output/ebpf_collector.bpf.o %{buildroot}/usr/lib

# xalarm
sh build/build.sh -i %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 600 config/xalarm.conf %{buildroot}%{_sysconfdir}/sysSentry
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/xalarm
install -m 600 service/xalarmd.service %{buildroot}%{_unitdir}
install -m 600 config/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/sysSentry
install -m 644 src/libso/xalarm/register_xalarm.h %{buildroot}%{_includedir}/xalarm/register_xalarm.h

# sentryCollector
install -m 600 config/collector.conf %{buildroot}%{_sysconfdir}/sysSentry
install -m 600 service/sentryCollector.service %{buildroot}%{_unitdir}

# cpu sentry
install config/tasks/cpu_sentry.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/cpu_sentry.ini %{buildroot}/etc/sysSentry/plugins/cpu_sentry.ini
install src/c/catcli/catlib/build/cat-cli %{buildroot}%{_bindir}/cat-cli
install src/c/catcli/catlib/build/plugin/cpu_patrol/libcpu_patrol.so %{buildroot}%{_libdir}

chrpath -d %{buildroot}%{_bindir}/cat-cli
chrpath -d %{buildroot}%{_libdir}/libcpu_patrol.so

# avg_block_io
install config/tasks/avg_block_io.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/avg_block_io.ini %{buildroot}/etc/sysSentry/plugins/avg_block_io.ini

# ai_block_io
install config/tasks/ai_block_io.mod %{buildroot}/etc/sysSentry/tasks/
install config/plugins/ai_block_io.ini %{buildroot}/etc/sysSentry/plugins/ai_block_io.ini

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
%dir %attr(0550,root,root) %{python3_sitelib}/xalarm
%attr(0550,root,root) %{python3_sitelib}/syssentry
%attr(0550,root,root) %{python3_sitelib}/sentryCollector
%attr(0550,root,root) %{python3_sitelib}/sentryPlugins/avg_block_io
%attr(0550,root,root) %{python3_sitelib}/sentryPlugins/ai_block_io

# sysSentry
%attr(0500,root,root) %{_bindir}/sentryctl
%attr(0550,root,root) %{_bindir}/syssentry
%attr(0750,root,root) %config(noreplace) %{_var}/log/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/plugins
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/inspect.conf
%attr(0600,root,root) %{_unitdir}/sysSentry.service
%attr(0755,root,root) %{_bindir}/ebpf_collector
%attr(0700,root,root) /usr/lib/ebpf_collector.bpf.o

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

# pysentry_collect
%exclude %{python3_sitelib}/sentryCollector/collect_plugin.py
%exclude %{python3_sitelib}/sentryCollector/__pycache__/collect_plugin*

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

%files -n pysentry_collect
%attr(0550,root,root) %{python3_sitelib}/sentryCollector/collect_plugin.py
%attr(0550,root,root) %{python3_sitelib}/sentryCollector/__pycache__/collect_plugin*

%changelog
* Mon Oct 21 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-54
- Type:bugfix
- CVE:NA
- SUG:NA
- DES:update collect plugin period max

* Mon Oct 21 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-53
- Type:bugfix
- CVE:NA
- SUG:NA
- DES:fix xalarm non-uniform logging format

* Mon Oct 21 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-52
- Type:bugfix
- CVE:NA
- SUG:NA
- DES:ai_block_io lack section exit

* Wed Oct 16 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-51
- Type:bugfix
- CVE:NA
- SUG:NA
- DES:fix ebpf iodump warning

* Wed Oct 16 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-50
- Type:bugfix
- CVE:NA
- SUG:NA
- DES:enrich alert info about kernel stack

* Wed Oct 16 2024 jinsaihang <jinsaihang@h-partners.com> - 1.0.2-49
- Type:bugfix
- CVE:NA
- SUG:NA
- DES:optimize log printing

* Wed Oct 16 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-48
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix ebpf miss kyqli rq_driver data

* Wed Oct 16 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-47
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix ai_block_io root cause bug

* Wed Oct 16 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-46
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:listen thread of collect module exits occasionally

* Tue Oct 15 2024 gaoruoshu <gaoruoshu@huawei.com> - 1.0.2-45
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:refactor config.py and bugfix uncorrect slow io report

* Mon Oct 14 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-44
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:ai_block_io fix some bugs

* Mon Oct 14 2024 jinsaihang <jinsaihang@h-partners.com> - 1.0.2-43
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix word error

* Mon Oct 14 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-42
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix dead loop when find next bpf map key

* Mon Oct 14 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-41
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:precise alarm query time.patch

* Sat Oct 12 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-40
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add pysentry_collect package and update collect log
       modify abnormal stack when the disk field is not configured

* Sat Oct 12 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-39
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add root cause analysis

* Sat Oct 12 2024 zhuofeng <zhangnan134@huawei.com> - 1.0.2-38
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix io_dump for collect module

* Sat Oct 12 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-37
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix ebpf collect iodump

* Fri Oct 11 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-36
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:ai_block_io support stage and iotype

* Fri Oct 11 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-35
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix xalarm upgrade not return val, not refuse to send msg when length exceeds 8192,cleanup invalid socket peroidlly

* Fri Oct 11 2024 jinsaihang <jinsaihang@h-partners.com> - 1.0.2-34
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add parameter valication for time_range and alarm_id and alarm_clear_time

* Fri Oct 11 2024 gaoruoshu <gaoruoshu@huawei.com> - 1.0.2-33
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:avg_block_io adapt different type of disk, use different config

* Thu Oct 10 2024 heyouzhi <heyouzhi.com> - 1.0.2-32
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:ai_block_io adapt alarm module

* Thu Oct 10 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-31
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add get_disk_type and fix some bugs
       add log for improving maintainability

* Thu Oct 10 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-30
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:xalarm add alarm msg length restriction to 8192

* Thu Oct 10 2024 jinsaihang <jinsaihang@h-partners.com> - 1.0.2-29
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add dependency for sysSentry and avg_block_io

* Thu Oct 10 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-28
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:modify iodump threhold from 1000 to 1000000000 and fix iodump in right turn

* Wed Oct 9 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-27
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix ai_block_io config relative some issues

* Wed Oct 9 2024 hubin <hubin73@huawei.com> - 1.0.2-26
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix get_alarm length and timestamp

* Wed Oct 9 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-25
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:update ebpf log

* Wed Oct 9 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-24
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:update log when it is not lock collect

* Wed Oct 9 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-23
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:avg_block_io send alarm to xalarmd

* Wed Oct 9 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-22
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix python 3.7 not support list[bool] type

* Tue Oct 8 2024 jinsaihang <jinsaihang@h-partners.com> - 1.0.2-21
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add alarm event query function

* Tue Oct 8 2024 caixiaomeng <caixiaomeng2@huawei.com> - 1.0.2-20
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add pyxalarm and pySentryNotify, add multi users support for xalarmd

* Mon Sep 30 2024 zhangnan <zhangnan134@huawei.com> - 1.0.2-19
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add ebpf collector

* Mon Sep 30 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-18
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix ai_block_io some issues

* Fri Sep 27 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-17
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add log level and change log format

* Wed Sep 25 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-16
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:fix bug step 2 about collect module and avg block io

* Mon Sep 23 2024 heyouzhi <heyouzhi@huawei.com> - 1.0.2-15
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add ai threshold slow io detection plugin

* Fri Sep 20 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-14
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:fix some about collect module and avg block io

* Sat Sep 14 2024 zhuofeng <zhuofeng2@huawei.com> - 1.0.2-13
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add collect module and avg_block_io plugin to sysSentry

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

