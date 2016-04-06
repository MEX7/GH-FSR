#!/usr/bin/env bash

# TODO 以后可以将地址以及要执行的脚本作为地址传入
# 参数初始化
project="outsourcing-erp-angularjs"
project_url="/opt/""$project"
folder="/opt/script_log/"
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
git reset --hard
echo "当前节点 "$(git reset --hard) >> "$folder""$file"
git pull

cd ${folder}
echo $(date "+%Y-%m-%d %H:%M:%S")" $project oerp_v1_reload 脚本执行成功" >> "$file"