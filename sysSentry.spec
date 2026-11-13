# Copyright (c) Huawei Technologies Co., Ltd. 2014-2023. All rights reserved.
# Description: spec file for package syssentry

Summary: System Inspection Framework
Name: sysSentry
Version: 1.0.3
Release: 55%{?dist}
License: Mulan PSL v2
Group: System Environment/Daemons
ExclusiveArch: x86_64 aarch64
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
Patch54:   delete-tmp-log-file-in-logrotate-syssentry.patch
Patch55:   delete-useless-sentry_urma_comm-mod-file.patch
Patch56:   fix-the-potential-KeyError-exception-in-task_get_ala.patch
Patch57:   fix-potential-stack-overflow-issue-in-hbm_online_rep.patch
Patch58:   fix-potential-crash-issue-in-bmc_recv.patch
Patch59:   fix-period-type-task-abnormal-status.patch
# PR-295
Patch60:   fix-potential-overflow-in-report_result.patch
Patch61:   fix-potential-memory-leak-issues-in-sentry_msg_monit.patch
Patch62:   fix-some-codecheck-warning.patch
Patch63:   set-log-level-in-sentry_msg_monitor.patch
# PR-300
Patch64:   fix-the-problem-of-checking-the-return-value-of-the-.patch
# PR-301
Patch65:   xalarm-add-sysSentry.service-status-monitoring.patch
Patch66:   refact-xalarm_unregister_event-and-xalarm_report_eve.patch
Patch67:   refact-sentryctl-set-cmd.patch
Patch68:   Implement-systemd-socket-activation-for-xalarm-and-f.patch
Patch69:   implement-systemd-socket-activation-for-sysSentry.patch
# PR-296
Patch70:   fix-potential-resource-leak-in-get_debugfs_dir.patch
Patch71:   fix-potential-buffer-overflow-in-create_trace_instan.patch
Patch72:   fix-potential-double-free-in-sentry_msg_monitor.patch
Patch73:   add-cmd-security-check.patch
Patch74:   add-exception-handling-for-sentryCollector.patch
Patch75:   fix-potential-DoS-attack-risks-and-resource-leaks.patch
Patch76:   change-some-msg-log-level.patch
Patch77:   fix-memset-usage.patch
Patch78:   fix-potential-memory-leak-in-print_map_res.patch
Patch79:   fix-potential-null-pointer-reference-in-extract_devi.patch
Patch80:   fix-crash-in-cpu_alarm.patch
Patch81:   use-snprintf-instead-of-sprintf-strcpy-strncpy.patch
Patch82:   fix-build-warning.patch
Patch83:   check-cpu-info-in-parse_patrol_result.patch
Patch84:   fix-potential-null-pointer-reference-in-catlib.patch
Patch85:   fix-socket-fd-leaks.patch
Patch86:   fix-NameError-in-task_get_alarm.patch
# PR-303
Patch87:   fix-fd-leaks-in-get_socket_id.patch
Patch88:   fix-resource-leaks-in-ebpf_collector.patch
Patch89:   fix-fd-leaks-in-sysSentry-and-xalarmd-service.patch
Patch90:   fix-potential-overflow-which-cause-the-allocated-mem.patch
Patch91:   fix-fd-leaks-in-sentry_msg_monitor.patch
# PR-299
Patch92:   rename-bmc_block_io-to-bmc_ras_sentry.patch
Patch93:   BMC-Ras-Sentry-add-config-bmc_events.patch
Patch94:   Support-report-bmc-block-ras-sentry.patch
# PR-302
Patch95:   bmc_ras_sentry-add-new-way-to-get-disk-SN-to-block-n.patch
Patch96:   bmc_ras_sentry-add-way-to-get-disk-SN.patch
# PR-305
Patch97:   delete-cmd-security-check.patch
# PR-304
Patch98:   feat-add-OOM-rate-limit-policy-configuration-support.patch
# PR-306
Patch99:   check-pid-result-and-add-some-log.patch
# PR-307
Patch100:  add-some-error-info.patch
# PR-311
Patch101:  fix-integer-overflow-rish-in-QueryEvents.patch
# PR-312
Patch102:  fix-potential-fd-leak-issue.patch
Patch103:  fix-the-infinite-loop-for-cleanup_thread-thread.patch
Patch104:  fix-error-log-for-task-stop-function.patch
# PR-316
Patch105:  feat-xalarm-add-event-registration-and-switch-manage.patch
Patch106:  compile-cpu_sentry-plugin.patch
# PR-328
Patch107:  change-os-name-in-service-desc.patch
Patch108:  delete-sensitive-information-content.patch
# PR-332
Patch109:  fix-build-warning-for-catlib.patch
# PR-338
Patch110:  fix-keep-critical-events-enabled-during-service-shut.patch
# PR-336
Patch111:  xalarm-auto-load-driver-when-proc-not-found.patch
# PR-337
Patch112:  fix-xalarm-fix-service-stop-timeout-and-PID-lock-rel.patch
Patch113:  fix-xalarm-add-graceful-shutdown-for-GLib-main-loop-.patch
Patch114:  update-bmc_ras_sentry-plugin.patch
Patch115:  fix-sysSentry-service-restart-issues-PID-lock-releas.patch
Patch116:  feat-add-link-event-alarm-reporting.patch
Patch117:  fix-event-switch-invalidation-after-sysSentry-servic.patch
Patch118:  verify-event-switch-state-by-reading-proc-file-befor.patch
Patch119:  feat-sentry_msg_monitor-add-kernel-driver-version-co.patch
Patch120:  fix-script-check-if-driver-exists-before-removing-it.patch
Patch121:  cleanup-uninstall-log_utils.h-file.patch
Patch122:  fix-PYNAME-define.patch
Patch123:  fix-security-build-options-bug-for-ebpf_collector.patch
Patch124:  Fix-the-issue-of-missing-security-compilation-option.patch
Patch125:  fix-bmc_ras_sentry-compile-failed-on-old-gcc.patch
Patch126:  fix-potential-overflow-in-xalarm_report_event.patch
Patch127:  Fix-CTL-message-length-overflow-when-data-exceeds-3-.patch
Patch128:  Fix-partial-send-recv-write-in-socket-communication.patch
Patch129:  fix-build-warning-v2.patch
Patch130:  Remove-unnecessary-operations-for-creating-var-run-s.patch
Patch131:  Create-the-socket-object-only-after-checking-if-the-.patch
Patch132:  add-validation-to-prevent-path-traversal-attacks.patch
Patch133:  fix-codecheck-warning.patch
Patch134:  improve-error-handling.patch
Patch135:  check-sock-value-in-create_unix_socket.patch
Patch136:  install-rasdaemon.mod-config-file.patch
Patch137:  delete-the-RPATH-from-libxalarm.so.patch
Patch138:  Enable-CMAKE_VERBOSE_MAKEFILE-to-show-detailed-compi.patch
Patch139:  Correct-the-misuse-of-compilation-options.patch
Patch140:  Do-not-allow-users-to-configure-unsafe-environment-v.patch
Patch141:  add-lock-to-protect-ALARM_REGISTER_INFO.patch
Patch142:  Check-whether-the-pointer-passed-to-report_result-is.patch
Patch143:  Fix-potential-memory-leak-in-report_result.patch
Patch144:  Return-failure-when-an-exception-occurs-while-parsin.patch
Patch145:  add-command-string-validation-to-prevent-command-inj.patch
Patch146:  enable-test_cpu_sentry.patch
Patch147:  cpu_sentry-lifts-the-runtime-dependency-on-libxalarm.patch
Patch148:  fix-check-__CPU_ALLOC-return-value-for-NULL-in-cli_e.patch
Patch149:  fix-check-config-black_list-NULL-pointer-in-tc_ring_.patch
Patch150:  fix-use-ln-snf-instead-of-ln-sf-for-symlink-creation.patch
Patch151:  fix-strlen-buf-1-underflow-on-empty-line-in-non-stan.patch
Patch152:  fix-check-strtok_r-NULL-return-in-catlib-plugins.patch
Patch153:  fix-set-restrictive-umask-0o077-instead-of-umask-0-i.patch
Patch154:  fix-resolve-PID-file-TOCTOU-race-conditions.patch
Patch155:  fix-verify-D-Bus-signal-sender-in-xalarm_server.py.patch
Patch156:  Add-exception-handling-for-sentryctl-exec-func-to-pr.patch
Patch157:  Unify-os.unlink-exception-handling.patch
Patch158:  Fix-security-issues-in-monitor_sentry_service-functi.patch
Patch159:  use-SignalMatch.remove-instead-of-bus.remove_signal_.patch
Patch160:  Add-test-cases-to-verify-whether-there-are-ERROR-lev.patch
Patch161:  Fix-type-mismatch-warning-and-add-I-O-size-limit-in-.patch
Patch162:  Fix-uninitialized-memory-read-in-string_to_ascii_hex.patch
Patch163:  Fix-NULL-deref-and-memory-leak-in-print_map_res.patch
Patch164:  Add-missing-blank-lines-to-improve-code-readability.patch
Patch165:  Add-copyright-information-to-cpu_alarm.py.patch
Patch166:  Use-isinstance-instead-of-type-comparison-for-type.patch
Patch167:  Avoid-sys.exit-outside-the-main-entry-in-cpu_sentry.patch
Patch168:  Remove-redundant-UnicodeError-catch.patch
Patch169:  Replace-sys.stderr.write-with-logging-in-pyxalarm.patch
Patch170:  Use-lazy-formatting-in-logging-calls.patch
Patch171:  Wrap-long-lines-to-keep-line-length-within-120-chars.patch
Patch172:  Handle-KeyError-when-collecting-data-detector.patch
Patch173:  Add-validation-for-the-return-value-of-regcomp-in.patch
Patch174:  Ensure-null-termination-of-error-strings-in.patch
Patch175:  Fix-block-device-check-logic-in-ebpf_collector.patch
Patch176:  Simplify-io_type-extraction-in-print_map_res.patch
Patch177:  Use-recv_all-to-prevent-partial-socket-data.patch
Patch178:  Close-the-accepted-client-socket-in-the.patch
Patch179:  Pass-the-absolute-path-to-the-external-command-call.patch
Patch180:  Add-more-insecure-environment-variables-to-the.patch
Patch181:  Add-validation-for-the-return-value-of.patch
Patch182:  Harden-string_to_ascii_hex-against-uninitialized.patch
Patch183:  Add-command-timeout-and-improve-error-reporting-in.patch
Patch184:  Add-explicit-guard-for-core-id-bitmap-capacity-in.patch
Patch185:  Reject-unaligned-size-in-tc_ring_one_space_init.patch
Patch186:  Validate-raid-tool-output-before-building-shell.patch
Patch187:  Harden-HexAsciiToChar-against-untrusted-ipmitool.patch
Patch188:  Fix-uint8_t-column-index-wraparound-hang-in.patch
Patch189:  Fix-out-of-bounds-read-in-ebpf_collector-when-log.patch
Patch190:  Fix-uncaught-exceptions-in-check_conflict-when.patch
Patch191:  Fix-uncaught-exceptions-in-check_conflict-when-ad50a6cf.patch
Patch192:  Handle-xalarm-registration-timeout-to-prevent.patch
Patch193:  Reduce-xalarmd-registration-timeout-from-500ms-to.patch
Patch194:  fix-client_socket-leak-in-bmc_recv-on-success-path.patch
Patch195:  fix-TypeError-and-socket-leak-when-msg_head_process.patch
Patch196:  Fix-typos-in-variable-names-macros-and-log-messages.patch
Patch197:  Remove-unregister_events-action-to-protect-kernel.patch
Patch198:  Use-RecvAll-in-alarm_recv-to-handle-partial-stream.patch
Patch199:  fix-match-conflict-processes-by-exact-proc-cmdline.patch
Patch200:  fix-xalarm_UnRegister-hangs-when-alarm_recv-blocks.patch
Patch201:  delete-unnecessary-import-modules.patch
Patch202:  add-usleep-backoff-in-receiver_thread-loop.patch
Patch203:  add-check-for-alarm_id-alarm_clear_time-env_file-con.patch
Patch204:  Fix-build-warnings-in-the-sentry_msg_monitor-plugin.patch
Patch205:  xalarm-fix-subscriber-alarm-loss-from-stream-desync.patch

BuildRequires: cmake gcc-c++
BuildRequires: python3 python3-setuptools
BuildRequires: json-c-devel
BuildRequires: chrpath
BuildRequires: elfutils-devel clang libbpf-devel bpftool
BuildRequires: python3-numpy python3-pytest
BuildRequires: numactl-libs numactl-devel systemd-rpm-macros

Provides:      pyxalarm = %{version}-%{release}
Obsoletes:     pyxalarm < 1.0.3-25
Requires:      libbpf nvme-cli
Requires:      python3-dbus dbus-daemon python3-gobject-base

%define PYTHON_VERSION %{python3_version}
%define PKGVER syssentry-%{version}-py%{PYTHON_VERSION}.egg-info

%description
sysSentry provides framework tools for system inspection.

%package -n libxalarm
Summary:        The xalarm library for the sysSentry
Requires:       json-c
Requires:       sysSentry = %{version}-%{release}
Provides:       libxalarm = %{version}-%{release}

%description -n libxalarm
This package provides xalarm library for the sysSentry.

%package -n libxalarm-devel
Summary:        The development package for the libxalarm
Requires:       libxalarm = %{version}-%{release}
Requires:       json-c-devel
Provides:       libxalarm-devel = %{version}-%{release}

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

%package -n cpu_sentry
Summary:        CPU fault inspection program
Requires:       procps-ng
Recommends:     sysSentry = %{version}-%{release}
Recommends:     ipmitool

%description -n cpu_sentry
This package provides CPU fault detection

%package -n hbm_online_repair
Summary:        hbm_online_repair for the sysSentry
Provides:       hbm_online_repair = %{version}-%{release}
BuildRequires:  libtraceevent-devel
Requires:       libtraceevent ipmitool
Requires:       sysSentry = %{version}-%{release}

%description -n hbm_online_repair
This package provides hbm_online_repair for the sysSentry.

%ifarch aarch64
%package -n sentry_msg_monitor
Summary:        A plugin for sysSentry to listening specific messages
Requires:       sysSentry = %{version}-%{release}
Provides:       sentry_msg_monitor = %{version}-%{release}
BuildRequires:  libobmm-devel
Requires:       lsof libobmm ipmitool

%description -n sentry_msg_monitor
This package provides a plugin for sysSentry to listening specific messages
%endif

%package -n bmc_ras_sentry
Summary:        bmc_ras_sentry for the sysSentry
Provides:       bmc_ras_sentry = %{version}-%{release}
BuildRequires:  json-c-devel
Requires:       libxalarm ipmitool json-c
Requires:       sysSentry = %{version}-%{release}

%description -n bmc_ras_sentry
This package provides bmc_ras_sentry for the sysSentry.

%package -n soc_ring_sentry
Summary:        soc_ring_sentry for the sysSentry
Provides:       soc_ring_sentry = %{version}-%{release}
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
%systemd_preun xalarmd.socket sysSentry.socket xalarmd.service sysSentry.service sentryCollector.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart xalarmd.socket sysSentry.socket xalarmd.service sysSentry.service sentryCollector.service

%files
%defattr(-,root,root)
%attr(-,root,root) %{python3_sitelib}/xalarm
%attr(-,root,root) %{python3_sitelib}/syssentry
%attr(-,root,root) %{python3_sitelib}/%{PKGVER}
%attr(-,root,root) %{python3_sitelib}/sentryCollector

# sysSentry
%attr(-,root,root) %{_bindir}/sentryctl
%attr(-,root,root) %{_bindir}/syssentry
%attr(-,root,root) %{_bindir}/ebpf_collector
%attr(-,root,root) %config(noreplace) %{_var}/log/sysSentry
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/plugins
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/task_scripts
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/inspect.conf
%attr(-,root,root) %{_unitdir}/sysSentry.service
%attr(-,root,root) %{_unitdir}/sysSentry.socket
%attr(-,root,root) %{_libdir}/libsentry_log.so
%attr(-,root,root) %{_libdir}/libsentry_io.so

# pysentry_collect
%exclude %{python3_sitelib}/sentryCollector/collect_plugin.py
%exclude %{python3_sitelib}/sentryCollector/__pycache__/collect_plugin.*.pyc
# pysentry_notify
%exclude %{python3_sitelib}/xalarm/sentry_notify.py
%exclude %{python3_sitelib}/xalarm/__pycache__/sentry_notify.*.pyc

%exclude %{_sysconfdir}/sysSentry/tasks/ai_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/ai_block_io.ini
%exclude %{_sysconfdir}/sysSentry/tasks/avg_block_io.mod
%exclude %{_sysconfdir}/sysSentry/plugins/avg_block_io.ini
%exclude %{_sysconfdir}/sysSentry/tasks/bmc_ras_sentry.mod
%exclude %{_sysconfdir}/sysSentry/plugins/bmc_ras_sentry.ini

# cpu inspection module
%exclude %{_sysconfdir}/sysSentry/tasks/cpu_sentry.mod
%exclude %{_sysconfdir}/sysSentry/plugins/cpu_sentry.ini
%exclude %{_bindir}/cpu_sentry
%exclude %{_bindir}/cat-cli

# xalarm
%attr(-,root,root) %{_bindir}/xalarmd
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/xalarm.conf
%attr(-,root,root) %{_unitdir}/xalarmd.socket
%attr(-,root,root) %{_unitdir}/xalarmd.service

# logrotate
%dir %{_localstatedir}/lib/logrotate-syssentry
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/logrotate-sysSentry.conf
%attr(-,root,root) %{_sysconfdir}/cron.hourly/logrotate-sysSentry

# sentryCollector
%attr(-,root,root) %{_bindir}/sentryCollector
%attr(-,root,root) %{_sysconfdir}/sysSentry/collector.conf
%attr(-,root,root) %{_unitdir}/sentryCollector.service

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
%attr(-,root,root) %{_libdir}/libxalarm.so

%files -n libxalarm-devel
%dir %{_includedir}/xalarm
%attr(-,root,root) %{_includedir}/xalarm
%attr(-,root,root) %{_includedir}/xalarm/register_xalarm.h

%files -n pysentry_notify
%attr(-,root,root) %{python3_sitelib}/xalarm/sentry_notify.py
%attr(-,root,root)%{python3_sitelib}/xalarm/__pycache__/sentry_notify.*.pyc

%files -n avg_block_io
%attr(-,root,root) %{_bindir}/avg_block_io
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/avg_block_io.mod
%attr(-,root,root) %{_sysconfdir}/sysSentry/plugins/avg_block_io.ini
%attr(-,root,root) %{python3_sitelib}/sentryPlugins/avg_block_io

%files -n ai_block_io
%attr(-,root,root) %{_bindir}/ai_block_io
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/ai_block_io.mod
%attr(-,root,root) %{_sysconfdir}/sysSentry/plugins/ai_block_io.ini
%attr(-,root,root) %{python3_sitelib}/sentryPlugins/ai_block_io

%files -n pysentry_collect
%attr(-,root,root) %{python3_sitelib}/sentryCollector/collect_plugin.py
%attr(-,root,root) %{python3_sitelib}/sentryCollector/__pycache__/collect_plugin.*.pyc

%files -n cpu_sentry
%attr(-,root,root) %{_bindir}/cat-cli
%attr(-,root,root) %{_bindir}/cpu_sentry
%attr(-,root,root) %{_libdir}/libcpu_patrol.so
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/cpu_sentry.mod
%attr(-,root,root) %{_sysconfdir}/sysSentry/plugins/cpu_sentry.ini
%attr(-,root,root) %{python3_sitelib}/sentryPlugins/cpu_sentry

%files -n hbm_online_repair
%attr(-,root,root) %{_bindir}/hbm_online_repair
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/hbm_online_repair.env
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/hbm_online_repair.mod
%attr(-,root,root) %{python3_sitelib}/syssentry/bmc_alarm.py
%attr(-,root,root) %{python3_sitelib}/syssentry/__pycache__/bmc_alarm.*.pyc

%ifarch aarch64
%files -n sentry_msg_monitor
%attr(-,root,root) %{_bindir}/sentry_msg_monitor
%attr(-,root,root) %{_sysconfdir}/sysconfig/sentry_msg_monitor.env
%attr(-,root,root) %{_sysconfdir}/sysSentry/tasks/sentry_msg_monitor.mod
%attr(-,root,root) %{_sysconfdir}/sysSentry/task_scripts/sentry_msg_monitor.sh
%endif

%files -n bmc_ras_sentry
%attr(-,root,root) %{_bindir}/bmc_ras_sentry
%attr(-,root,root) %{_sysconfdir}/sysSentry/plugins/bmc_ras_sentry.ini
%attr(-,root,root) %{_sysconfdir}/sysSentry/tasks/bmc_ras_sentry.mod

%files -n soc_ring_sentry
%attr(-,root,root) %{_bindir}/soc_ring_sentry
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/soc_ring_sentry.env
%attr(-,root,root) %config(noreplace) %{_sysconfdir}/sysSentry/tasks/soc_ring_sentry.mod

%changelog
* Fri Nov 13 2026 Zhou Haoran <zhouhaoran30@huawei.com> - 1.0.3-55
- [Type] sync
- [DESC] synchronize version to opencloudos repository

* Mon Jul 13 2026 shenyangyang <1014938109@qq.com> - 1.0.3-1
- [Type] sync
- [DESC] Package init
