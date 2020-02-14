# Chapter 0_1. PyCharm的安装和配置

----
Author: W.Y.  
Date: 2019/12/31  
Update: 2020/2/13  
Info: PyCharm的安装和配置

----
## 1. 关于Pycharm和Jupyter Notebook的选择
1. Pycharm和Jupyter Notebook都是Python的IDE，可以理解为R studio和R的关系。
2. 通常说法是新手用Jupyter Notebook，大项目用Pycharm。也还有其它的IDE，或者不用IDE直接cmd运行Python都可以。

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

## 2. Pycharm的安装

1. [下载网址](https://www.jetbrains.com/pycharm/)
2. 下载电脑对应的版本即可。下载Community版本就可以，是免费的。用Community版本是完全够的，非常够！
3. 同样，一路`Next`，直到这步，
必须勾选`Add launchers dir to the PATH`，强烈建议勾选`Add "Open Folder as Project"`。如图：  
![如图](https://github.com/git-wy/SimplePython/blob/master/%E5%9B%BE%E7%89%87/Pycharm%E5%AE%89%E8%A3%85%2001.png?raw=true)
4. 后面基本上没啥，一路完成就可以。
5. Community版本到这里就结束了。如果确实想用Professional版本，可以自行百度怎么激活。也可以提供一对一服务~


## 3. 打开Pycharm

这时候，你已经安装好了Anaconda和Pycharm。那我们就打开Pycharm开始吧。

两种方式打开Pycharm：
1. 双击Pycharm应用打开，需要create new project
2. 选择一个文件夹，右键文件夹，选择`Open Folder as PyCharm Project`。（前提是安装时勾选了这个选项）

**NOTE**
> Pycharm中的Project可以理解为一个文件夹，里面可以放很多Files，包括各种文件类型。
>比如这次的教程，我都存在一个SimplePython的文件夹中，在Pycharm中打开就是一个同名的Project，里面包括数据、代码、说明等等文件，还有子文件夹等。

## 4. Pycharm中设置解释器
1. 打开Pycharm之后，在`File | Settings | Project: [Project的名称] | Project Interpreter`里面设置
2. 在Project Interpreter中，点击小齿轮，选择`Add`，如图：  
![图片](https://github.com/git-wy/SimplePython/blob/master/%E5%9B%BE%E7%89%87/Pycharm%20%E8%AE%BE%E7%BD%AE%E8%A7%A3%E9%87%8A%E5%99%A8%2001.png?raw=true)
3. 应该会出现几种环境的选择，通常会有以下四种，如图：  
![图片](https://github.com/git-wy/SimplePython/blob/master/%E5%9B%BE%E7%89%87/Pycharm%20%E8%AE%BE%E7%BD%AE%E8%A7%A3%E9%87%8A%E5%99%A8%2002.png?raw=true)
4. 简单介绍一下，主要是前三种比较常用：  
4.1 Virtualenv Environment：虚拟环境，可以理解为每个Project都重新配置，是相互独立的，模块不通用。我不太建议，如果有多个Python版本同时使用的话，可以用这个。   
4.2 Conda Environment：就是通过Anaconda安装的话，会有这个环境下的解释器。我用的是这个。   
4.3 System Environment：直接安装Python，就是系统里安装的Python的解释器。  
4.4 Pipenv Environment：用pip安装的解释器，我也没用过。  
5. 设置解释器：  
5.1 如果是用Anaconda安装的Python，那么就类似我的设置，在`Conda Environment | Existing environment`中，设置为自己的Anaconda安装路径下的Python路径即可。如图：  
![图片](https://github.com/git-wy/SimplePython/blob/master/%E5%9B%BE%E7%89%87/Pycharm%20%E8%AE%BE%E7%BD%AE%E8%A7%A3%E9%87%8A%E5%99%A8%2003.png?raw=true)  
5.2 如果是直接安装的Python，那就选择`System Environment`，设置为自己的Python安装路径下的Python.exe即可。  


>1. 如果还不是太清楚，百度一下就好了。各位的搜索能力我还是相信的~
>2. 作为一个假~~程序员~~，还是强烈建议直接用英文版本的，不要用汉化了。


## 5. 设置字符编码
通常源代码我们用的是utf-8的字符编码。
1. Pycharm中可以在`File | Settings | Editor | File Encodings`里面设置。
2. 在Python文件（扩展名是`.py`）中要声明文件所使用的编码，在文件第一行加入`# -*- coding: utf-8 -*-`。


**SUMMARY**
> 以上就完成了基本的配置。