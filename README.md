# sysSentry

#### 介绍
sysSentry is a system inspection framework used to manage system inspection tasks.

#### 软件架构
1. 框架：支持x86和aarch64架构
2. 插件：不同的差距支持架构不同，请参考docs.openeuler.org中的内容


#### 安装教程

1.  安装巡检框架
```shell
[root@openEuler ~]# yum install -y sysSentry
```
2.  启动巡检框架
```shell
[root@openEuler ~]# systemctl start sentryCollector
[root@openEuler ~]# systemctl start xalarmd
[root@openEuler ~]# systemctl start sysSentry
```
3.  安装&重载巡检插件
step1. 安装用户需要的巡检插件
```shell
yum install <插件名>
```
当前支持插件有：
- cpu_sentry -- cpu巡检，支持22.03-LTS-SP4版本，aarch64架构，920F芯片使用
- avg_block_io -- 平均阈值慢io检测，支持20.03-LTS-SP4版本，x86及aarch64架构
- ai_block_io -- AI阈值慢io检测，支持20.03-LTS-SP4版本，x86及aarch64架构

step2. 重载巡检插件
```shell
[root@openEuler ~]# sentryctl reload <插件名>
```

#### 使用说明

sysSentry提供了用于管理巡检插件的命令 -- sentryctl，可以用于启动/停止巡检插件任务、查看巡检插件运行状态、查看巡检插件上报信息等功能。

1. 启动指定巡检任务

   ```shell
   [root@openEuler ~]# sentryctl start <module_name>
   ```

2. 终止指定巡检任务

   ```shell
   [root@openEuler ~]# sentryctl stop <module_name>
   ```

3. 列出所有已加载的巡检任务及状态

   ```shell
   [root@openEuler ~]# sentryctl list
   ```

4. 查询指定巡检任务的状态

   ```shell
   [root@openEuler ~]# sentryctl status <module_name>
   ```

   巡检任务共存在四种状态，每种状态的回显信息及对应介绍如下：

   | 状态    | 描述                                                         |
   | ------- | ------------------------------------------------------------ |
   | RUNNING | 巡检任务正在运行                                             |
   | WAITING | 仅period类型巡检任务可设置此状态，表示period巡检任务等待下一次被调度执行 |
   | EXITED  | 巡检任务尚未执行，或者oneshot类型的巡检任务执行结束处于此状态 |
   | FAILED  | 巡检任务未拉起成功，或者巡检任务未正常退出                   |

5. 重载指定巡检任务的配置

   当用户修改了巡检任务的配置文件/etc/sysSentry/tasks/<module_name>.mod时，可通过以下命令重载配置文件：

   ```shell
   [root@openEuler ~]# sentryctl reload <module_name>
   ```

6. 查询指定任务的告警信息

   ```shell
   [root@openEuler ~]# sentryctl get_alarm <module_name> [options]
   ```

   options可选参数及释义如下：

   | 参数                                   | 描述                                                         |
   | -------------------------------------- | ------------------------------------------------------------ |
   | -s TIME_RANGE, --time_range TIME_RANGE | 展示用户指定时间长度内的告警信息，TIME_RANGE为整形，单位秒，范围为1~15 |
   | -d, --detailed                         | 打印详细告警信息                                             |

7. 查询指定巡检任务的巡检结果

   ```shell
   sentryctl get_result <module_name>
   ```




#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request