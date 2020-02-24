# Chapter 4_1. 利用腾讯API进行语音转文字

----
Author: W.Y.  
Date: 2020/2/24  
Update: 2020/2/24  
Info: 调用腾讯API，进行录音文件转写，实现语音转文字。主要是这个代码文件`TencentAudio2Text.py`的实现方式。

----

## 1. 获取腾讯API密钥
1. 首先要有腾讯云账号，[进入腾讯云官网](https://cloud.tencent.com/)，登录或注册账号
2. 进入控制台，[网址](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)
3. 在控制台界面，右上角个人界面下，进入`访问管理`。如图：
![](https://github.com/git-wy/SimplePython/blob/master/%E5%9B%BE%E7%89%87/Chapter%204/%E8%85%BE%E8%AE%AFAPI%20%E8%AE%BF%E9%97%AE%E7%AE%A1%E7%90%86%2001.png?raw=true)
4. 在访问管理界面中，选择`访问密钥 | API密钥管理`。如图：
![](https://github.com/git-wy/SimplePython/blob/master/%E5%9B%BE%E7%89%87/Chapter%204/%E8%85%BE%E8%AE%AFAPI%20%E5%AF%86%E9%92%A5%E7%AE%A1%E7%90%86%2001.png?raw=true)
5. 双击进入，可以不管提示直接进入。点击`新建密钥`。
6. 生成的密钥部分，SecretId和SecretKey是我们需要的。


> 可以了解一下腾讯云关于录音文件转写的官方文档[点击跳转](https://cloud.tencent.com/document/product/1093/37823)

## 2. 需要的模块及其安装

1. 打开windows的cmd
2. 输入以下代码，等待安装完成即可：
``` python
pip install tencentcloud-sdk-python
```

> 其它需要的模块除了pandas都是标准库，不需要另外安装，可以直接调用。


## 3. 运行

1. 下载`TecentAudio2Text.py`文件，可以存在一个文件夹A中。
2. 把语音数据（`.wav`或`.mp3`等常见格式都可以）都保存在一个文件夹B中即可
3. 然后最好把B文件夹放在A文件夹里面。然后用Pycharm打开A文件夹作为一个Project即可。  
类似我这个文件夹，`TecentAudio2Text.py`文件存在`CH 4_1 语音转文字`这个文件夹，
数据在`Data`文件夹，`Data`文件夹在`CH 4_1 语音转文字`里面。运行的时候，将`CH 4_1 语音转文字`这个文件夹用Pycharm打开即可。
4. 用Pycharm打开后，在`TencentAudio2Text.py`中，有两处自定义设置区，按照注释修改即可。
5. 直接运行`TencentAudio2Text.py`即可。


