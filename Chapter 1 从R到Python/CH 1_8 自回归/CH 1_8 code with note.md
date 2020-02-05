# Chapter 1_8 自回归

----
Author: W.Y.  
Date: 2020/1/17  
Update: 2020/2/5  
Info: 王汉生老师书的第八章，自回归的python极简实现    

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [时间序列图](#3-时间序列图)
4. [描述性分析（箱图）](#4-描述性分析箱图)
5. [自相关系数](#5-自相关系数)
6. [自回归模型](#6-自回归模型)
7. [模型诊断](#7-模型诊断)
8. [预测](#8-预测)
9. [SUMMARY](#SUMMARY)

## 1. 导入模块
[回到目录](#content)

``` python
# 导入模块

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sma
from statsmodels.graphics.tsaplots import plot_acf  # 自相关系数图
from statsmodels.tsa.ar_model import AR  # 自回归模型
```

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据

data = pd.read_csv('E:\Data Mining\SimplePython\Chapter 1 从R到Python\CH 1_8 自回归\CH 1_8 data rate.csv')
```

## 3. 时间序列图
[回到目录](#content)

``` python
# 时间序列图

data['rate'].plot()
```

``` python
# 序列平稳

log_rate = pd.Series(np.diff(np.log(data['rate'])))
log_rate.plot()
```

## 4. 描述性分析（箱图）
[回到目录](#content)

``` python
# 描述性分析（箱图）

plt.boxplot(data['rate'])
```

``` python
plt.boxplot(log_rate)
```

## 5. 自相关系数
[回到目录](#content)

``` python
# 自相关系数

plot_acf(data['rate'], lags=30) 
```

``` python
plot_acf(log_rate, lags=30)
```

## 6. 自回归模型
[回到目录](#content)

``` python
# 自回归模型

model1 = AR(log_rate).fit(maxlag=4)
model1.params
```

**NOTE**
> 结果和R的有略微不同。因为R的默认method是yule-walker,而Python的这个模块，
> 作者不建议用yw的方法，因为无法计算constant。

``` python
model2 = AR(log_rate).fit(ic='aic')
model2.params  # 也是为2
```
## 7. 模型诊断
[回到目录](#content)

``` python
# 模型诊断
# 自相关系数图

plot_acf(model2.resid, lags=30)
```

``` python
# 残差图

model2.resid.plot()
```

``` python
# QQ图

sma.qqplot(model2.resid)
```

## 8.预测
[回到目录](#content)

### 8.1 预测一个值
``` python
log_rate1 = log_rate[0:600]
log_rate2 = log_rate[600]
```

``` python
model3 = AR(log_rate1).fit(maxlag=2)
model3.params
```

``` python
model3.predict(start=600,end=600)
```

### 8.2 预测多个值
``` python
log_rate_true = log_rate[600:706]
log_rate_true = log_rate_true.reset_index(drop=True)
```

``` python
log_rate_predict = list()   # 创建一个新的列表（list）
for i in range(0,107):  # 在0到107内（左闭右开）循环
    log_rate_i = log_rate[i:600+i]  # 选择前600个值
    model_i = AR(log_rate_i).fit(maxlag=2)   # 用前600个值建模
    predict = pd.DataFrame(model_i.predict(start=600, end=600).values)  # 预测下一个值
    log_rate_predict.append(predict[0][0])  # 把预测值存入列表
```

**NOTE**
> 这里是每次都用前600个值预测后一个值，所以要写一个循环  

``` python
df_log_rate_predict = pd.Series(log_rate_predict)  # 保存预测值
```

``` python
# 预测误差

np.mean((df_log_rate_predict-log_rate_true)**2)/np.var(log_rate_true)
```

``` python
# 真实值和预测值的比较

plt.plot(log_rate_true,color='green', label='True value' )
plt.plot(df_log_rate_predict, color='red', label='Predicted value')
plt.legend()
```
## SUMMARY
[回到目录](#content)

> 后面几章也不是特别常用，所以就没有很详细了，就非常简单的实现一下，过一遍就好了。

