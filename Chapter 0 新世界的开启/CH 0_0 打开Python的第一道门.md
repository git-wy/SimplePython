# Chapter 0_0. 打开Python的第一道门

----
author: W.Y.  
first_edition: 2019/12/31  
last_edition: 2020/1/14  
description: Python的安装、设置、运行

----

## 1. Python的安装

1. 建议通过Anaconda进行安装（[Anaconda下载地址](https://www.anaconda.com/distribution/)）  
2. 按照自己的电脑版本，下载Python 3.7 version  
3. 安装过程中，需要勾选 Add Anaconda to my_PATH environment variable
和 Register Anaconda as my default Python 3.7  
4. 检查是否安装成功（windows）：进入电脑cmd（命令提示符）（Windows可用`win+R`打开运行，输入cmd打开命令提示符）。
输入`python`，如果出现Python版本，说明安装成功。


>1. 如果安装不成功或有其他问题，请自行百度。或私聊，提供一对一服务，欸嘿~  
>2. 我电脑是windows，所以设置啥的都是以windows版本为准，Mac版本就自行解决吧~


## 2. 关于Pycharm和Jupyter Notebook的选择
1. Pycharm和Jupyter Notebook都是Python的IDE，可以理解为R studio和R的关系。   
2. 通常说法是新手用Jupyter Notebook，大项目用Pycharm。  

但我个人觉得Pycharm好用。原因有三：  
a. Pycharm看起来更高大上。尤其是暗黑模式，非常有黑客的感jio~  
b. Pycharm数据库功能强大，查看、整理数据很方便。  
c. Pycharm有很多插件，也有阉割版的Jupyter Notebook,两全其美！所以为啥不直接用Pycharm呢~  
（唯一的缺点就是耗内存）

>我用的就是Pycharm，所以很多设置什么的都是以Pycharm为准。
>如果用Jupyter Notebook，有不一样的地方就只能自行百度了~
>（没错！就是要你跟我一起用Pycharm~哈哈哈）

#### 2.1 Pycharm的安装
1. [下载网址](https://www.jetbrains.com/pycharm/)
2. 下载Community版本就可以，是免费的。用Community版本是完全够的，非常够！
3. 如果确实想用Professional版本，可以自行百度怎么激活。也可以提供一对一服务~

## 3. 关于环境变量
要把Anaconda，Python，和Pycharm或者Jupyter Notebook的安装路径都添加到系统的环境变量
（具体请百度，懒得写了）


## 4. 设置解释器
这时候，你已经安装好了Anaconda和Pycharm。那我们就打开Pycharm开始吧。

两种方式：
1. 新打开Pycharm时，会要create new project。需要设置Interpreter, 就选择Anaconda安装路径下面的python.exe就可以。
2. 已经打开某个project, 可以在`File | Settings | Project: SimplePython | Project Interpreter`里面设置。


>1. 一两句话可能说的不是太清楚，百度一下就好了。各位的搜索能力我还是相信的~
>2. 作为一个假~~程序员~~，还是强烈建议直接用英文版本的，不要用汉化了。


## 5. 设置字符编码
通常源代码用的是utf-8的字符编码。
1. Pycharm中可以在`File | Settings | Editor | File Encodings`里面设置。
2. 在Python文件中要声明文件所使用的编码，在文件第一行加入`# -*- coding: utf-8 -*-`。


## 6. Hello World!
以上设置好之后，就可以开始运行了！看到标题，大家应该都懂的。

1. 在Project中，右键New→Python File，命名，新建文件。
2. 在看起来很高级的界面，输入`print("hello world")`。Run!
3. 搞定。第一个Python程序就运行成功了！是不是超级简单！？



**SUMMARY**
>1. 没啥可说的，这章的目的就是安装好、配置好、能运行就可以。
>2. 最终可以成功`print("hello world")`就可以。不成功的，请百度，或者从头再看一遍这个文档~