# webssh
## 介绍
一个简单的Web应用程序，用作连接到ssh服务器的ssh客户端。它是用Python编写的，基于channels、paramiko和xterm.js。

## 功能
- 支持SSH密码验证，包括空密码。
- 支持SSH公钥认证，包括DSA RSA ECDSA Ed25519密钥。
- 支持加密密钥。
- 支持全屏终端。
- 终端窗口可调整大小。
- 自动检测ssh服务器的默认编码。
- 现代浏览器支持Chrome，Firefox，Safari，Edge，Opera。

## webssh演示过程截图
### ssh登录界面
![webssh1](https://github.com/devopssec/webssh/blob/master/static/img/webssh1.png)
### 命令行界面
![webssh2](https://github.com/devopssec/webssh/blob/master/static/img/webssh2.png)
### top交互式命令行界面
![webssh3](https://github.com/devopssec/webssh/blob/master/static/img/webssh3.png)

## 这个怎么运作
    +---------+     http     +--------+    ssh    +-----------+
    | browser | <==========> | webssh | <=======> | ssh server|
    +---------+   websocket  +--------+    ssh    +-----------+
    
## 安装:(Centos 7 环境)
    # 部署webssh
	$ git clone https://github.com/devopssec/webssh.git
	$ sudo yum -y install epel-release gcc python36 python36-devel
	$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	$ sudo python3.6 get-pip.py
	$ sudo python3.6 -m pip install Django==1.11.7 paramiko==2.4.1 channels==2.1.6
    # 迁移数据库
	$ cd webssh/
	$ python3.6 manage.py makemigrations
	$ python3.6 manage.py migrate
	# 启动服务
	$ python3.6 manage.py runserver 0.0.0.0:8000

