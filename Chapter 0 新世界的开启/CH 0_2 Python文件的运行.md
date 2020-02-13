# Chapter 0_1. Python文件的运行

----
Author: W.Y.  
Date: 2020/1/3  
Update: 2020/2/13  
Info: Python文件的运行  

----

## 6. Hello World!
以上设置好之后，就可以开始运行了！看到标题，大家应该都懂的。

1. 在Project中，右键，New→Python File，命名，新建文件。
2. 在看起来很高级的界面，输入`print("hello world")`。Run!
3. 搞定。第一个Python程序就运行成功了！是不是超级简单！？



## 1. Python模块的基础用法
#### 1.1 安装模块：
1. 直接打开cmd，用`pip install module_name` 可以安装相应模块
2. 比如`pip install pandas`。（如果通过Anaconda安装Python，很多常用模块已经下载好了）
3. 通常报错`No module named 'XXX'`的时候，就是没有安装模块。需要`pip install`一下


关于`pip install`和`pip3 install`：
> 1. 可以简单理解为版本不同，如果只安装了Python3两个命令是没有区别的。
> 2. 如果安装了Python 2.x和Python 3.x，`pip install`会安装在Python 2.x路径下，那用Python 3.x运行的时候就不能`import`了
> 正常应该不会有这个问题的。
> 3. 下面也是一样的。


#### 1.2 更新模块：
1. `pip install --upgrade module_name`
2. 比如，`pip install --upgrade pandas`


## 2. Pycharm中的一些有用的设置
#### 2.1 设置模板
`File | Settings | Editor | File and Code Templates`。可以设置Python Script的模板。
比如我的：
```python
# -*- coding: utf-8 -*-
# Author: W.Y.
# Date: ${DATE}
```
这样每次新建一个Python文件，都会有这些。看起来是不是就比较高级了？哈哈哈~

#### 2.2 插件
Pycharm有很丰富的插件。在`File | Settings | Plugins`中查找、下载、启用。
推荐3个：
1. Jupyter Notebook （没错，就是他！可以在Pycharm里面用Jupyter Notebook）
2. Markdown （Markdown语法也是超好用的，这次的教程基本上就是用Markdown写的）
3. Database Navigator （数据库，可以用mySQL，SQLite等等，要处理非常多的数据的时候很好用）

还有其它的插件可以自己去发掘吧~~



## 3. 小小的tips （持更）
1. `help()`函数，类似R中，可以看到函数的介绍和基本用法。比如`help("print")`。
如果是函数名，可以直接用`help(print)`，如果是某些运算符，则需要用引号，比如`help("lambda")`。
总而言之，建议都加上引号。
2. `ctrl + 鼠标左键点击函数名`，可看到函数源代码和参数说明等。


**SUMMARY**
>1. 本章主要是基础用法，Pycharm的一些设置和Python的一些小tips。
>2. 初步的介绍目前就到这里了。关于正常教程的那些，什么基本语法，什么列表、字典那些令人头大的，这里是没有的。
>毕竟这是个不正常的教程。我jio得这些都可以在后面的实际应用中慢慢体会。
>3. 如果需要非常详细的教程，建议看官方文档。贴心给大家附上官方的中文版文档 [点这里点这里](https://docs.python.org/zh-cn/3/tutorial/index.html)