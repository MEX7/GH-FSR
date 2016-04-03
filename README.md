# GH-FSR  
> 利用Git的hooks来完成项目的自动发布的功能，基于Flask框架直接调用linux上的shell脚本（bash）   
> git hooks flask shell release 简写 GH-FSR  


## 功能构想
- 自动部署脚本(目前这个对于例如java这样的项目来说还不能自动编译，所以自动编译的部分需要其他工具完成再调用这个就可以了)
- API管理(上传API文档，文档提供两级目录，分别对应项目和模块）


## 启动方式
基于**Gunicorn**
[参考文档](http://docs.jinkan.org/docs/flask/deploying/wsgi-standalone.html)
