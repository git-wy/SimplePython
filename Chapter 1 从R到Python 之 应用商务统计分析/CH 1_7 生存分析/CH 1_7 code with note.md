# Chapter 1_7 生存分析

----
Author: W.Y.  
Date: 2020/1/16  
Update: 2020/2/5  
Info: 王汉生老师书的第七章，生存分析的python极简实现   

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [生存函数图](#3-生存函数图)
4. [AFT模型](#4-AFT模型)
5. [COX模型](#5-COX模型)
6. [SUMMARY](#SUMMARY)

## 1. 导入模块
[回到目录](#content)

``` python
# 导入模块

import pandas as pd
import matplotlib.pyplot as plt  
import lifelines
```

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据

data = pd.read_csv('E:\Data Mining\SimplePython\Chapter 1 从R到Python\CH 1_7 生存分析\CH 1_7 data.csv')
```

``` python
# 预览数据

data.head(20)
```

## 3. 生存函数图
[回到目录](#content)

``` python
# 生存函数图

kmf = lifelines.KaplanMeierFitter()
kmf.fit(data['Time'], event_observed=data['VStatus'])

kmf.plot()
```

``` python
data['status'] = data['HGB'].apply(lambda x: 1 if x>data['HGB'].median() else 0)
```

``` python
kmf = lifelines.KaplanMeierFitter()
HGB_group = (data['status'] == 1)
 
kmf.fit(data['Time'][~HGB_group], data['VStatus'][~HGB_group], label='HGB<Median')
ax = kmf.plot()
 
kmf.fit(data['Time'][HGB_group], data['VStatus'][HGB_group], label='HGB>Median')
kmf.plot(ax=ax)
```

``` python
kmf = lifelines.KaplanMeierFitter()
Platelet = (data['Platelet'] == 1)
 
kmf.fit(data['Time'][~Platelet], data['VStatus'][~Platelet], label='abnormal')
ax = kmf.plot(ci_show=False)
 
kmf.fit(data['Time'][Platelet], data['VStatus'][Platelet], label='normal')
kmf.plot(ax=ax, ci_show=False)
```

``` python
kmf = lifelines.KaplanMeierFitter()
Age = (data['Age'] > data['Age'].median())
 
kmf.fit(data['Time'][~Age], data['VStatus'][~Age], label='Age<60')
ax = kmf.plot(show_censors=True, ci_show=False)
 
kmf.fit(data['Time'][Age], data['VStatus'][Age], label='Age>60')
kmf.plot(ax=ax,show_censors=True, ci_show=False)
```

``` python
kmf = lifelines.KaplanMeierFitter()
LogWBC = (data['LogWBC'] > data['LogWBC'].median())
LogPBM = (data['LogPBM'] > data['LogPBM'].median())
Protein = (data['Protein'] > data['Protein'].median())
SCalc = (data['SCalc'] > data['SCalc'].median())

kmf.fit(data['Time'][~LogWBC], data['VStatus'][~LogWBC], label='LogWBC<median')
kmf.plot(ax=plt.subplot(2,2,1), show_censors=True, ci_show=False)
kmf.fit(data['Time'][LogWBC], data['VStatus'][LogWBC], label='LogWBC>median')
kmf.plot(ax=plt.subplot(2,2,1),show_censors=True, ci_show=False)

kmf.fit(data['Time'][~LogPBM], data['VStatus'][~LogPBM], label='LogPBM<median')
kmf.plot(ax=plt.subplot(2,2,2), show_censors=True, ci_show=False)
kmf.fit(data['Time'][LogPBM], data['VStatus'][LogPBM], label='LogPBM>median')
kmf.plot(ax=plt.subplot(2,2,2),show_censors=True, ci_show=False)

kmf.fit(data['Time'][~Protein], data['VStatus'][~Protein], label='Protein<median')
kmf.plot(ax=plt.subplot(2,2,3), show_censors=True, ci_show=False)
kmf.fit(data['Time'][Protein], data['VStatus'][Protein], label='Protein>median')
kmf.plot(ax=plt.subplot(2,2,3),show_censors=True, ci_show=False)

kmf.fit(data['Time'][~SCalc], data['VStatus'][~SCalc], label='SCalc<median')
kmf.plot(ax=plt.subplot(2,2,4), show_censors=True, ci_show=False)
kmf.fit(data['Time'][SCalc], data['VStatus'][SCalc], label='SCalc>median')
kmf.plot(ax=plt.subplot(2,2,4),show_censors=True, ci_show=False)
```

## 4. AFT模型
[回到目录](#content)

``` python
# AFT模型

weibull = lifelines.WeibullAFTFitter()

weibull.fit(data.iloc[:,0:9], duration_col='Time', event_col='VStatus')
weibull.print_summary()
```

## 5. COX模型
[回到目录](#content)

``` python
# Cox模型

cox = lifelines.CoxPHFitter()
cox.fit(data.iloc[:,0:9], duration_col='Time', event_col='VStatus')
cox.print_summary()  
```

## SUMMARY
[回到目录](#content)

> 后面几章也不是特别常用，所以就没有很详细了，就非常简单的实现一下，过一遍就好了。

