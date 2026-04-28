#!/bin/bash

set -euo pipefail

# 设置错误捕获：打印失败的行号和命令
trap 'echo "❌ 错误发生在第 $LINENO 行，命令: $BASH_COMMAND" >&2' ERR

# 检查参数数量
if [ $# -ne 2 ]; then
  echo "用法: $0 <pkg_name> <pkg_version>"
  echo "示例: $0 syssentry 1.0.3"
  exit 1
fi

# 接收参数
pkg_name="$1"
pkg_version="$2"

# 定义文件名和目录名
orig_tar="${pkg_name}_${pkg_version}.orig.tar.gz"
source_dir="${pkg_name}-${pkg_version}"

rm -rf ${source_dir}

# 重命名源码包
if [ -f "${pkg_name}-${pkg_version}.tar.gz" ]; then
  echo "重命名源码包为: ${orig_tar}"
  cp -f "${pkg_name}-${pkg_version}.tar.gz" "${orig_tar}"
else
  echo "错误: 未找到源码包 ${pkg_name}-${pkg_version}.tar.gz"
  exit 1
fi

# 自动安装构建依赖
apt-get build-dep . -y

# 创建并进入源码目录
echo "创建源码目录: ${source_dir}"
mkdir -p "${source_dir}"
pushd "${source_dir}" > /dev/null

# 解压源码包
echo "解压源码包到当前目录"
tar -xzf "../${orig_tar}" --strip-components=1

# 执行dh_make生成debian目录框架
echo "生成debian目录结构"
dh_make -y -l

# 拷贝上层目录的debian自定义配置
if [ -d "../debian" ]; then
  echo "拷贝自定义debian配置"
  cp -ar ../debian/* ./debian/
else
  echo "警告: 上层目录未找到debian目录，将使用默认配置"
fi

# 构建deb包
echo "开始构建deb包"
dpkg-buildpackage -rfakeroot -us -uc

# 退出源码目录
popd > /dev/null

echo "打包完成，生成的包文件在当前目录"
