# Chapter 1_5 定序回归

----
Author: W.Y.  
Date: 2020/1/16  
Update: 2020/2/5  
Info: 王汉生老师书的第五章，定序回归的python极简实现  

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [描述性分析](#3-描述性分析)
4. [定序回归](#4-定序回归)
5. [SUMMARY](#SUMMARY)

## 1. 导入模块
[回到目录](#content)

``` python
# 导入模块

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import linear_ordinal_regression as ordinal
```

**NOTE**
> 1. 没有合适的做定序回归的模块，所以还是找了github上某位大神的函数。
>参考[原链接](https://github.com/Shopify/bevel)。
> 2. 我只借用了其中`linear_ordinal_regression.py`这个文件。
> 3. 要用这个模块，需要安装其它模块，请参考[requirements](https://github.com/Shopify/bevel/blob/master/requirements.txt)。
>列在下面：  
>3.1 numpy>=1.13.3  
>3.2 scipy>=1.0.0  
>3.3 pandas>=0.21.0  
>3.4 numdifftools>=0.9.20

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据

data = pd.read_csv('E:/Data Mining/SimplePython/Chapter 1 从R到Python/CH 1_5 定序回归/CH 1_5 data ceilphone.csv')
```

``` python
# 预览数据

data.head()
```

## 3. 描述性分析
[回到目录](#content)


``` python
# 列联表

w1_table = pd.crosstab(index=data['score'], columns=data['W1'], values=data['score'], aggfunc='count')
print(w1_table)
```

``` python
# 画图

plt.plot(data.groupby('score')['W2'].mean(),'o-',color='black')
plt.xticks(range(1,6,1))
plt.yticks(np.arange(0,1,0.2))
plt.xlabel('score')
plt.ylabel('percentage')
plt.title('Digital Camera')
```

``` python
fig, ax = plt.subplots(2,2,sharex='all', sharey='all')  
ax[0][0].plot(data.groupby('score')['W3'].mean(),'o-',color='black')
ax[0][0].set_ylim(0,1)
ax[0][0].set_xlabel('score')
ax[0][0].set_ylabel('percentage')
ax[0][0].set_title('Television')
ax[0][1].plot(data.groupby('score')['W4'].mean(),'o-',color='black')
ax[1][0].plot(data.groupby('score')['W5'].mean(),'o-',color='black')
ax[1][1].plot(data.groupby('score')['W6'].mean(),'o-',color='black')
```

``` python
# 列联表

w7_table = pd.crosstab(index=data['score'], columns=data['W7'], values=data['score'], aggfunc='count')
print(w7_table)
```


## 4. 定序回归
[回到目录](#content)

**NOTE**
> 1. 找了很久找到的这个模块，但是不支持字符串变量和分类变量，所以无法实现和书上一样的定序回归  
> 2. 所以下面就是随便弄了一下，暂时没有解决这个问题。暂时搁置吧

``` python
# 将字符串变量编码为数值型

data['W1_code'] = pd.Categorical(data['W1']).codes
X = data.iloc[:,2:9]
```

### 4.1 Probit回归

``` python
# Probit

probit1 = ordinal.OrderedProbit().fit(X, data['score'])
print(probit1.print_summary())
```
 
### 4.2 Logit回归

``` python
# Logit

logit1 = ordinal.OrderedLogit().fit(X, data['score'])
print(logit1.print_summary())
```

## SUMMARY
[回到目录](#content)

>1. 这章没有成功解决，暂时这样吧~

