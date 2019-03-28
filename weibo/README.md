[TOC]



# 使用说明

## 安装环境

1. 打开cmd，切换到 all 目录：`cd C:\Users\ocstar\Desktop\all`

2. 创建python虚拟环境 `pipenv shell`

   ![](.\pictures\图像 001.png)

   虚拟环境创建成功是这种效果：

   ![](.\pictures\图像 002.png)

3. 安装依赖：执行下面的命令

   ```
   pip install Twisted-18.9.0-cp36-cp36m-win_amd64.whl
   pip install -r requirements.txt
   ```

   看到下面的 successfully installed 就好。

   ![](.\pictures\图像 003.png)



## 代理池

1. 确认在虚拟环境里面

2. 进入 proxy_pool 目录，执行 `python run.py` ，会出现如下效果。

   ![](.\pictures\图像 004.png)

3. 代理池会进行代理IP的获取和验证，然后存入mongo数据库，同时在本地的 5010端口 启动web服务器 提供api接口。

4. 运行几十秒后，查看mongodb 是否成功获得了 代理IP。成功后应该有两张表，如下所示

   ![](.\pictures\图像 005.png)

5. 打开浏览器，输入 `http://localhost:5010/get/` , 随机获取一个代理IP。成功效果如下

   ![](.\pictures\图像 006.png)

6. ctrl + c  这个组合键 可以关闭 代理池



## cookies池

1. 确认进入了虚拟环境

2. 切换到` CookiePolls`  文件夹，导入账号，最后输入`exit` 退出

   ![](.\pictures\图像 007.png)

3. 执行 `python run.py` 启动cookie池, 同时会启动 5000端口对外提供api。

   ![](.\pictures\图像 008.png)

4. 所有的cookie和账号，会放到redis中维护，然后定时检测是否失效。打开redis查看，成功效果如下

   ![](.\pictures\图像 009.png)

5. 用浏览器测试API，检查是否能随机获取cookie，浏览器中输入 `http://localhost:5000/weibo/random` ,成功效果如下:

   ![](.\pictures\图像 010.png)



## 运行爬虫

1. 确认进入虚拟环境

2. 切换到爬虫目录，执行 `python main.py`

   ![](.\pictures\图像 011.png)

3. 稍等一下，会出现类似如下效果，表示成功：

   ![](.\pictures\图像 012.png)





## 分布式

在其他主机上配置好环境，把爬虫代码拷贝过去，（不要拷贝代理池，cookie池）。

然后执行 python main.py 运行就好。

注意在settings.py中，修改好 数据库和redis的地址。

![](.\pictures\图像 013.png)

在所有代码里面，把上面红线标志的地址换成 你的windows主机的地址就好了，可以用 ipconfig 命令查看地址

![](.\pictures\图像 014.png)

