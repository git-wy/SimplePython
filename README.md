SimplePython
----

#### 闲话
>1. 这个其实算我自己边学边整理的笔记，不是很规范的教程，仅供参考~  
>2. 我也是边学边整理，很多知识我也不是完全清楚，只有大概的了解，如果想准确、深入的了解还是自己查资料吧。  
>3. 很多函数、代码可能并不是最优、最简的，
>一方面是因为只是为了能解决问题，如果学有余力，还可以看看如何优化代码；
>另一方面，是因为我自己也没有学到家。  
>4. 按Python代码的规范，注释并不是越多越好，但是耐不住我废话多。


#### 注意
1. 建议的学习顺序：  
1.1 最开始必须看Chapter 0  
1.2 然后按照Chapter 1 → Chapter 2的顺序。（从R到Python这两章，是为大家量身定做的~希望能够帮到大家！）  
1.3 非常建议学完前三章再学Chapter 3、4、5，这三章没有先后，可以选择性学习  
1.4 番外篇可以选择性学习，或者有需要的时候看。  

# Chapter 0 新世界的开启
**INFO**
> 关于Python的安装、设置，Pycharm的安装、配置等  
> 闲话多多，干货少少的一章~

**CONTENT**
1. Python的安装 [初步完结](https://github.com/git-wy/SimplePython/blob/master/Chapter%200%20%E6%96%B0%E4%B8%96%E7%95%8C%E7%9A%84%E5%BC%80%E5%90%AF/CH%200_0%20Python%E7%9A%84%E5%AE%89%E8%A3%85.md)
2. PyCharm的安装和配置 [初步完结](https://github.com/git-wy/SimplePython/blob/master/Chapter%200%20%E6%96%B0%E4%B8%96%E7%95%8C%E7%9A%84%E5%BC%80%E5%90%AF/CH%200_1%20PyCharm%E7%9A%84%E5%AE%89%E8%A3%85%E5%92%8C%E9%85%8D%E7%BD%AE.md)
3. Python文件的运行 [待完善]()
4. PyCharm的小Tips [持更中]()

# Chapter 1 从R到Python 之 应用商务统计分析

**INFO**
>1. 王汉生《应用商务统计分析》的python实现。因此背景、数据、结果说明等省略，直接参考书即可
>2. 很多模型我觉得用R跑更方便。后期会发现R做这类简单的统计分析代码更简洁。
>这里仅作为从R到python的一个过渡、熟悉过程，中间穿插一些python的基本知识。


**NOTE** 
>1. 这是最开始写的一章，所以比较详细，每节都分为两个版本：  
>1.1 包括代码和结果的、可运行的code版本。这部分的代码都是基于Jupyter Notebook的格式，在Pycharm中是拓展名为`.ipynb`的文件，逐行运行，
>方便理解每步的结果。方式也更像R，我觉得可能更好入门。（后面章节形式可能会不太一样）  
>1.2 包括代码和详细注释、无法直接运行的Markdown版本。  
>2. 建议的学习方式是，下载数据，对照两个版本，自己敲（~~复制~~）代码，然后仔细品一品代码、结果和注释
>3. 注意看代码中`#`后面的说明和提示，注意看`NOTE`部分的注释。闲话写的到处都是，所以请仔细看各个地方的备注和注释哦
>4. 因为分两个版本太浪费时间了，所以只有这一章用了这个形式，后面都直接在code版本里面加的注释。
>可能注释看起来比较乱，但是比较节省我的时间，请大家谅解了!


**GOAL**
>1. 掌握模块`pandas`, `numpy`, `statsmodels`, `matplotlib`等的基本用法
>2. 掌握数据读取、数据基本处理等
>3. 掌握Python的基础语法和基础函数


**CONTENT**
1. 线性回归 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_1%20%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92)
2. 方差分析 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_2%20%E6%96%B9%E5%B7%AE%E5%88%86%E6%9E%90)
3. 协方差分析 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_3%20%E5%8D%8F%E6%96%B9%E5%B7%AE%E5%88%86%E6%9E%90)
4. 0-1回归 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_4%200-1%E5%9B%9E%E5%BD%92)
5. 定序回归 [未完成](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_5%20%E5%AE%9A%E5%BA%8F%E5%9B%9E%E5%BD%92)
6. 泊松回归 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_6%20%E6%B3%8A%E6%9D%BE%E5%9B%9E%E5%BD%92)
7. 生存分析 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_7%20%E7%94%9F%E5%AD%98%E5%88%86%E6%9E%90)
8. 自回归 [初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%201%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E5%BA%94%E7%94%A8%E5%95%86%E5%8A%A1%E7%BB%9F%E8%AE%A1%E5%88%86%E6%9E%90/CH%201_8%20%E8%87%AA%E5%9B%9E%E5%BD%92)


# Chapter 2 从R到Python 之 数据挖掘与应用
**INFO**
>1. 张俊妮《数据挖掘与应用》的python实现。同样，背景、数据、结果说明等省略，直接参考书即可
>2. 这本书很多模型比《应用商务统计分析》的更复杂，也有很多机器学习的内容，建议学习。


**NOTE**
1. 如前面说到的，从这章开始，只有带有注释的code版本了。
2. 注释穿插在代码中间，还有很多我的废话，大家仔细看哦~
3. 这本书是每章不止一个案例，所以我是每个案例都单独一个文件的。

**CONTENT**
1. 数据理解和数据准备[初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%202%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E4%B8%8E%E5%BA%94%E7%94%A8/CH%202_2%20%E6%95%B0%E6%8D%AE%E7%90%86%E8%A7%A3%E5%92%8C%E6%95%B0%E6%8D%AE%E5%87%86%E5%A4%87)  
1.1 case1: 数据整合  
1.2 case2: 数据准备  
2. 缺失数据[更新中](https://github.com/git-wy/SimplePython/tree/master/Chapter%202%20%E4%BB%8ER%E5%88%B0Python%20%E4%B9%8B%20%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98%E4%B8%8E%E5%BA%94%E7%94%A8/CH%202_3%20%E7%BC%BA%E5%A4%B1%E6%95%B0%E6%8D%AE)  
3. [待更新]()  


# Chapter 3 自然语言处理
[待更新]()

1. 利用腾讯API进行情感分析[初步完结]()

**INFO**
>简单的自然语言处理方法

**CONTENT**
（暂定，可能会调整）
1. 文本预处理
2. 情感分析
3. 主题分析

# Chapter 4 语音分析

[待更新]()
1. 利用腾讯API实现语音转文字[初步完结](https://github.com/git-wy/SimplePython/tree/master/Chapter%204%20%E8%AF%AD%E9%9F%B3%E5%88%86%E6%9E%90/CH%204_1%20%E8%AF%AD%E9%9F%B3%E8%BD%AC%E6%96%87%E5%AD%97)


# Chapter 5 爬虫
[待更新]()

1. 用户微博及其评论爬取[初步完结]()

**INFO**
>爬虫教程必推崔庆才大神！！！b站就有教程。易懂、好学、全面，就是特别全面，涉及很多内容。
>如果就想简单了解一下我们最可能、最常用的，可以参考这个小破教程~  

**CONTENT** 
（暂定，可能会调整）
1. 表格类型的数据爬取（以天气数据为例）
2. TripAdvisor数据爬取
3. Weibo数据爬取

# 番外篇
**INFO**
>1. 不知道怎么归类的乱七八糟的东西
>2. 可能算中级或高级用法，建议掌握的
>3. 很多都是常见的教程里会讲的，我个人觉得有些算是Python劝退的部分吧
>4. 可以不按照顺序，应该不会影响理解和学习

**CONTENT**
（暂定，可能会调整）

1. 番外一：条件判断和循环
2. 番外二：匿名函数（lambda）
2. 番外三：内置函数（map, reduce, filter等）
3. 番外四：自定义函数
4. 番外五：调用自定义模块 [初步完结](https://github.com/git-wy/SimplePython/blob/master/%E7%95%AA%E5%A4%96%E7%AF%87/%E7%95%AA%E5%A4%96%E4%BA%94%20%E8%B0%83%E7%94%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E6%A8%A1%E5%9D%97.md)
3. 番外六：调用API事半功倍

# APPENDIX：资源汇总

1. Python官方文档。[英文版](https://docs.python.org/3/tutorial/)，[中文版](https://docs.python.org/zh-cn/3/tutorial/index.html)