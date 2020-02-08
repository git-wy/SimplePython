# Chapter 1_2 方差分析

----
Author: W.Y.  
Date: 2020/1/1  
Update: 2020/2/3  
Info: 王汉生老师书的第二章，方差分析的Python极简实现  

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [描述性分析（画图）](#3-描述性分析画图)
4. [描述性分析（频数分布）](#4-描述性分析频数分布)
5. [方差分析](#5-方差分析)
6. [模型诊断（画图）](#6-模型诊断画图)
7. [预测](#7-预测)
8. [SUMMARY](#SUMMARY)

## 1. 导入模块
[回到目录](#content)

``` python
import pandas as pd   
import numpy as np  
import matplotlib.pyplot as plt   
import matplotlib  
import statsmodels.formula.api as smf   # 基于公式的数据分析模块statsmodels
import statsmodels.api as sma  # 数据分析模块statsmodels
import lmdiag   
import searborn as sns  # 画图模块
from statsmodels.stats.multicomp import pairwise_tukeyhsd  # 多重比较
```

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据之导入csv文件 

data_real = pd.read_csv('E:/Data Mining/SimplePython/Chapter 1 从R到Python/CH 1_2 方差分析/CH 1_2 data real.csv', encoding='gbk')  
data_new = pd.read_csv('E:/Data Mining/SimplePython/Chapter 1 从R到Python/CH 1_2 方差分析/CH 1_2 data new.csv', encoding='gbk')
```

**NOTE**
>因为文件中出现了中文，所以需要修改编码格式，用`encoding='gbk'`


## 3. 描述性分析（画图）
### 3.1 散点图

``` python
# 描述性分析（散点图）

sns.pairplot(data_real)  
```

**NOTE**

>1. 结果和R不同，因为前几个变量是字符串，Python没有自动编码成数值型，所以只画了数值型的变量的散点图。
>2. 所以下面将几个字符串型的变量编码为数值型，然后存入新的数据框，再次画图。

``` python
# 转换数据（把字符串编码为数值型）

data_plot = pd.DataFrame()
data_plot['dis'] = pd.Categorical(data_real['dis']).codes
data_plot['ring'] = pd.Categorical(data_real['ring']).codes
data_plot['wuye'] = pd.Categorical(data_real['wuye']).codes
data_plot['fitment'] = pd.Categorical(data_real['fitment']).codes
data_plot['contype'] = pd.Categorical(data_real['contype']).codes
```

``` python
# 再次画图

sns.pairplot(data_plot)  
```

### 3.2 箱图

``` python
# 描述性分析（箱图）

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus']=False  # 正常显示负号

sns.boxplot(x='ring',y='price',data=data_real, color='white',
           order=['二环以内', '二至三环', '三至四环', '四至五环', '五环以外'])  
```

**NOTE**
>1. `matplotlib`中也有箱图，但是好像只支持单个变量，不支持设置自变量和因变量，所以这里用了`searborn`模块
>2. `order = []`是设置x轴中各个类别的顺序，可以试试不加这个参数，比较一下不同


``` python
# 取对数

data_real['log_price'] = np.log(data_real['price'])  # 按书上的常规操作，取哈对数 
```

``` python
# 描述性分析（箱图，多图一起画）

sns.boxplot(x=data_real['dis'],y=data_real['log_price'], 
            color='white', ax=plt.subplot(2,2,1))  # 设置2×2的画布，选定第1副子图，即第一行第一个。下同
sns.boxplot(x=data_real['wuye'],y=data_real['log_price'], 
            color='grey', ax=plt.subplot(2,2,2))
sns.boxplot(x=data_real['fitment'],y=data_real['log_price'], 
            color='black', ax=plt.subplot(2,2,3))
sns.boxplot(x=data_real['contype'],y=data_real['log_price'], 
            ax=plt.subplot(2,2,4))
```

**NOTE**
>`plt.subplot(m, n, i)`设置子图，m行n列的画布，选定第i个。类似R中的`par(mfrow=c(m,n))	`


## 4. 描述性分析（频数分布）
[回到目录](#content)

``` python
# 描述性分析（频数分布）

print(data_real.dis.value_counts())
print(data_real.ring.value_counts())
print(data_real.fitment.value_counts())
print(data_real['wuye'].value_counts())
print(data_real['contype'].value_counts())
```

## 5. 方差分析
[回到目录](#content)

### 5.1 单因素方差分析
``` python
# 单因素方差分析

anova1 = smf.ols('log_price ~ C(ring)', data=data_real).fit()
print(sma.stats.anova_lm(anova1, typ=3))   # typ=3就是R中的type='III'
```

**NOTE**
>`statsmodels`中，设置因子型变量用`C(var)`，类似R中的`as.factor(var)`。
>本案例中是字符串型的数据，所以加不加无所谓，
>如果是数值型的分类数据，比如编码为1、2、3等，则需要加上`C()`，否则会视为连续变量。

``` python
# 查看具体每个水平的情况

print(anova1.summary())
```

``` python
# 多重比较

compare1 = pairwise_tukeyhsd(data_real['log_price'], data_real['ring'])
print(compare1.summary())   # reject = True就是拒绝原假设，说明两组差异显著。
```

### 5.2 多因素方差分析
``` python
# 多因素方差分析 （书里太啰嗦啦，直接多因素，就包括了单因素、双因素和交互作用）

anova2 = smf.ols('log_price ~ C(dis)*C(ring) + C(wuye) + C(fitment) +'
                  'C(contype)', data=data_real).fit()
print(sma.stats.anova_lm(anova2, typ=3))
```

**NOTE**
>1. 没错！看到了熟悉了*号，和R一样，也是用*号来表示交互作用的。
>2. 和R一样，`var1*var2`等同于`var1 + var2 + var1:var2`。

``` python
print(anova2.summary())
```

## 6. 模型诊断（画图）
[回到目录](#content)

``` python
lmdiag.plot(anova2)
```

**NOTE**
>1. 是不是报错了？？哈哈哈哈~
>2. 可能是因为加了交互项，有的水平是缺失的，所以画图不行。
>3. 下面用不加交互项的试试给你们看下

``` python
# 试试不用交互项的

anova_test = smf.ols('log_price ~ C(dis) + C(ring) + C(wuye) + C(fitment) +'
                  'C(contype)', data=data_real).fit()
lmdiag.plot(anova_test)
```


## 7. 预测
[回到目录](#content)

``` python
# 预测

predict = anova2.predict(data_new)
```

``` python
data_new['predict'] = np.exp(predict)  # 因为前面取了对数，所以这里再求指数
```

``` python
print(data_new)
```

## SUMMARY
[回到目录](#content)

>1. 这章没有什么新知识，所以也比较简单，注释也比较少。
>2. 主要有几点，需要掌握：  
>2.1 利用`pandas`读取csv文件  
>2.2 利用`pandas`将字符串数据重新编码  
>2.3 利用`searborn`画箱图   
>2.4 `statsmodels`中，设置因子型变量  

