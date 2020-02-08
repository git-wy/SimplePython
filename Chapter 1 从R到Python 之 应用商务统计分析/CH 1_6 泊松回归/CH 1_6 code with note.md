# Chapter 1_6 泊松回归

----
Author: W.Y.  
Date: 2020/1/15  
Update: 2020/2/5  
Info: 王汉生老师书的第六章，泊松回归的python极简实现   

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [描述性分析](#3-描述性分析)
4. [泊松回归](#4-泊松回归)
5. [变量选择](#5-变量选择)
6. [预测](#6-预测)
7. [SUMMARY](#SUMMARY)

## 1. 导入模块
[回到目录](#content)

``` python
# 导入模块

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import matplotlib
import seaborn as sns
import statsmodels.formula.api as smf  
```

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据

data = pd.read_csv('E:\Data Mining\SimplePython\Chapter 1 从R到Python\CH 1_6 泊松回归\CH 1_6 data crm.csv')
```

``` python
# 预览数据

data.head()
```

## 3. 描述性分析
[回到目录](#content)

``` python
# 描述性分析

df_describe = pd.concat([data.mean(),data.min(), 
                         data.median(),data.max(),
                         data.std()], axis=1)
df_describe.columns = ['mean', 'min', 'median', 'max', 'std']  # 重命名列名
df_describe
```

``` python
# 箱图

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus']=False  # 正常显示负号

sns.boxplot(x='freq0',y='freq1',data=data, color='white')  
```

``` python
sns.boxplot(x='freq0',y='exp1',data=data, color='white') 
```

``` python
# 箱图 （多图一起画）

fig = plt.figure(figsize=(8, 6))
sns.boxplot(x=data['freq0'],y=data['freq1'], color='grey',  
            ax=plt.subplot(2,3,1)).set_title("第-1月")
sns.boxplot(x=data['freq0'],y=data['freq2'], color='grey', 
            ax=plt.subplot(2,3,2)).set_title("第-2月")
sns.boxplot(x=data['freq0'],y=data['freq3'], color='grey',  
            ax=plt.subplot(2,3,3)).set_title("第-3月")
sns.boxplot(x=data['freq0'],y=data['exp1'], color='grey', 
            ax=plt.subplot(2,3,4)).set_title("第-1月")
sns.boxplot(x=data['freq0'],y=data['exp2'], color='grey',  
            ax=plt.subplot(2,3,5)).set_title("第-2月")
sns.boxplot(x=data['freq0'],y=data['exp3'], color='grey', 
            ax=plt.subplot(2,3,6)).set_title("第-3月")
fig.tight_layout()
```

## 4. 泊松回归
[回到目录](#content)

``` python
# 泊松回归

model1 = smf.poisson('freq0 ~ freq1 + freq2 + freq3 + '
                     'exp1 + exp2 + exp3', data).fit()
print(model1.summary())
```

## 5. 变量选择
[回到目录](#content)


**NOTE**
> `stepwiseSelection`函数不支持泊松回归，我也没有找到合适的方法，所以就省略这步了。


## 6. 预测
[回到目录](#content)

### 7.1 预测
``` python
# 预测

data_new = pd.read_csv('E:\Data Mining\SimplePython\Chapter 1 从R到Python\CH 1_6 泊松回归\CH 1_6 data new.csv')
data_new.head()
```

``` python
data_new['predict'] = model1.predict(data_new)
data_new.head()
```

``` python
# 绝对预测误差

np.sqrt(np.mean((data_new['freq0']-data_new['predict'])**2))
```

## SUMMARY
[回到目录](#content)

> 后面几章也不是特别常用，所以就没有很详细了，就非常简单的实现一下，过一遍就好了。

