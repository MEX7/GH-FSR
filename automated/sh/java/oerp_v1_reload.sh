#!/usr/bin/env bash

# TODO 以后可以将地址以及要执行的脚本作为地址传入
# 参数初始化
project="outsourcing-erp-java"
folder="/opt/script_log/"
project_url="/opt/""$project"
file=$(date +%Y-%m-%d)" ${project}.txt"

# 创建日志文件夹
if [ ! -d "$folder" ]; then
    mkdir "$folder"
fi
cd ${folder}

# 创建当前日期的log文件
if [ ! -f "$file" ]; then
    touch "$file"
fi

# 写入启动数据
echo $(date "+%Y-%m-%d %H:%M:%S")" $project oerp_v1_reload 脚本执行开始" >> "$file"


cd ${project_url}
/bin/bash project/application/bin/app stop
git reset --hard && git pull
echo "当前节点 "$(git reset --hard) >> "$folder""$file"
/bin/bash project/application/bin/app start

cd ${folder}
echo $(date "+%Y-%m-%d %H:%M:%S")" $project oerp_v1_reload 脚本执行成功" >> "$file"