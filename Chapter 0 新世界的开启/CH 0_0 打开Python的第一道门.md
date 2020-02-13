# Chapter 0_0. 打开Python的第一道门

----
Author: W.Y.  
Date: 2019/12/31  
Update: 2020/1/14  
Info: Python的安装、设置、运行

----

## 1. Python的安装（Windows版）

### 1.1 方法一：通过Anaconda安装（建议）

优点：
> 1. 包含了很多模块
> 2. 方便管理环境

缺点：
> 1. 因为包含了很多模块，所以安装包大，第一次安装比较麻烦，还占内存

安装过程：
> 1. [Anaconda下载地址](https://www.anaconda.com/distribution/)
> 2. 目前最新版本是Python 3.7 version，按照自己电脑版本下载对应的就行
> 3. 双击下载的`.exe`文件，点`Next`继续，根据提示一直继续
> 4. 到这一步，需要勾选 `Add Anaconda to my_PATH environment variable`
和 `Register Anaconda as my default Python 3.7`。![如图](https://raw.githubusercontent.com/git-wy/SimplePython/master/%E5%9B%BE%E7%89%87/Anaconda%E5%AE%89%E8%A3%85%2001.png)
> 5. 其它都选择默认，或者自己选择安装路径等等，没有关系，只有第4步注意一下。
> 6. 进入电脑cmd（命令提示符）（Windows用`win+R`打开运行，输入`cmd`，打开命令提示符）。
输入`python`，如果出现Python版本，说明安装成功


### 1.2 方法二：直接安装Python

优缺点我感觉就和Anaconda的相反。

安装过程：
> 1. [下载地址](https://www.python.org/downloads/)
> 2. 目前最新版本是3.8.1，Anaconda目前最新是3.7版本，对我们来说没有很大区别。
>根据自己电脑版本下载对应的就可以。
> 3. 双击下载的`.exe`文件，继续
> 4. 同理，要勾选`Add Python 3.8 to PATH`这个选项。![网上找的图]()
> 5. 同上面的方法，检查是否安装成功。


**NOTE**
1. 都要记得勾选`add to path`的选项，就是添加到系统环境变量。如果安装过程中勾选了，就没什么问题。
2. 如果没有勾选，自己百度添加吧，下面提到的IDE也都要添加到环境变量。如果实在不知道，那就重新安装一次，再勾选吧
3. 如果安装不成功或有其他问题，请自行百度。或私聊，提供一对一服务，欸嘿~  
4. 我电脑是windows，所以设置啥的都是以windows版本为准，Mac版本就自行解决吧~


## 2. 关于Pycharm和Jupyter Notebook的选择
1. Pycharm和Jupyter Notebook都是Python的IDE，可以理解为R studio和R的关系。   
2. 通常说法是新手用Jupyter Notebook，大项目用Pycharm。也还有其它的IDE，或者直接cmd运行都可以。  

但我个人觉得Pycharm好用：  
1. 看起来更高大上，非常有感jio~  
2. 项目管理很方便
3. 数据库功能强大，查看、整理数据很方便。  
4. 有很多插件，也有阉割版的Jupyter Notebook,两全其美！所以为啥不直接用Pycharm呢~  

也有缺点：
1. 内存、CPU占用高
2. 吃配置，配置低的话，可能会很卡。

>我用的就是Pycharm，所以很多设置什么的都是以Pycharm为准。
>如果用Jupyter Notebook或其它，有不一样的地方就只能自行百度了~
>（没错！就是要你跟我一起用Pycharm~哈哈哈）

## 3. Pycharm的安装

> 1. [下载网址](https://www.jetbrains.com/pycharm/)
> 2. 下载电脑对应的版本即可。下载Community版本就可以，是免费的。用Community版本是完全够的，非常够！
> 3. 同样，一路`Next`，直到这步，
>必须勾选`Add launchers dir to the PATH`，
>强烈建议勾选`Add "Open Folder as Project"`。
> 4. 后面基本上没啥，一路完成就可以。
> 5. Community版本到这里就结束了。如果确实想用Professional版本，可以自行百度怎么激活。也可以提供一对一服务~


## 4. Pycharm中设置解释器

### 4.1 方法一：
这时候，你已经安装好了Anaconda和Pycharm。那我们就打开Pycharm开始吧。

两种方式：
1. 新打开Pycharm时，会要create new project。需要设置Interpreter, 就选择Anaconda安装路径下面的python.exe就可以。
2. 已经打开某个project, 可以在`File | Settings | Project: SimplePython | Project Interpreter`里面设置。


>1. 一两句话可能说的不是太清楚，百度一下就好了。各位的搜索能力我还是相信的~
>2. 作为一个假~~程序员~~，还是强烈建议直接用英文版本的，不要用汉化了。


## 5. 设置字符编码
通常源代码我们用的是utf-8的字符编码。
1. Pycharm中可以在`File | Settings | Editor | File Encodings`里面设置。
2. 在Python文件（扩展名是`.py`）中要声明文件所使用的编码，在文件第一行加入`# -*- coding: utf-8 -*-`。


## 6. Hello World!
以上设置好之后，就可以开始运行了！看到标题，大家应该都懂的。

1. 在Project中，右键New→Python File，命名，新建文件。
2. 在看起来很高级的界面，输入`print("hello world")`。Run!
3. 搞定。第一个Python程序就运行成功了！是不是超级简单！？



**SUMMARY**
>1. 没啥可说的，这章的目的就是安装好、配置好、能运行就可以。
>2. 最终可以成功`print("hello world")`就可以。不成功的，请百度，或者从头再看一遍这个文档~