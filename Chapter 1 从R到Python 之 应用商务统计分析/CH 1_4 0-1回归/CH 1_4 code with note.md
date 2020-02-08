# Chapter 1_4 0-1回归

----
Author: W.Y.  
Date: 2020/1/15  
Update: 2020/2/5  
Info: 王汉生老师书的第四章，0-1回归的python极简实现  

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [描述性分析（画图）](#3-描述性分析画图)
4. [Logit回归](#4-Logit回归)
5. [Probit回归](#5-Probit回归)
6. [变量选择](#6-变量选择)
7. [预测](#7-预测)
8. [SUMMARY](#SUMMARY)

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
import stepwiseSelection
from sklearn import metrics  # 用于计算fpr和tpr
```

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据

data = pd.read_csv('E:/Data Mining/SimplePython/Chapter 1 从R到Python/CH 1_4 0-1回归/CH 1_4 data ST.csv')
```

``` python
# 数据分割

data1999 = data[data['year'] == 1999]
data2000 = data[data['year'] == 2000]
```

``` python
# 预览数据

data.head()
```

## 3. 描述性分析（画图）
[回到目录](#content)

``` python
# 箱图

sns.boxplot(data1999['ST'], data1999['ARA'],color='white')
```

``` python
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus']=False  # 正常显示负号

fig = plt.figure(figsize=(8, 6))
sns.boxplot(data1999['ST'], data1999['ASSET'], color='white', ax=plt.subplot(3,2,1)) 
sns.boxplot(data1999['ST'], data1999['ATO'], color='white', ax=plt.subplot(3,2,2))
sns.boxplot(data1999['ST'], data1999['GROWTH'], color='white', ax=plt.subplot(3,2,3))
sns.boxplot(data1999['ST'], data1999['LEV'], color='white',ax=plt.subplot(3,2,4))
sns.boxplot(data1999['ST'], data1999['ROA'], color='white',ax=plt.subplot(3,2,5))
sns.boxplot(data1999['ST'], data1999['SHARE'], color='white',ax=plt.subplot(3,2,6))
fig.tight_layout()
```

## 4. Logit回归
[回到目录](#content)

``` python
# Logit回归（全模型）

logit1 = smf.logit('ST ~ ARA + ASSET + ATO + GROWTH + '
                   'LEV + ROA + SHARE', data1999).fit()

print(logit1.summary())
```


## 5. Probit回归
[回到目录](#content)

``` python
# Probit回归（全模型）

probit1 = smf.probit('ST ~ ARA + ASSET + ATO + GROWTH + '
                   'LEV + ROA + SHARE', data1999).fit()

print(probit1.summary())
```

## 6. 变量选择
[回到目录](#content)

``` python
# 变量选择

X_train = data1999.iloc[:, 1:8]
```

### 6.1 AIC
``` python
# AIC 

logit_aic_vars, logit_aic_logs = stepwiseSelection.backwardSelection(X_train, data1999['ST'], model_type='logistic')
```

``` python
logit_aic = smf.logit('ST ~ ARA + GROWTH + LEV', data1999).fit()
print(logit_aic.summary())
```

### 6.2 BIC
``` python
# BIC

logit_bic_vars, logit_bic_logs = stepwiseSelection.backwardSelection(X_train, data1999['ST'], model_type='logistic', elimination_criteria='bic')
```

``` python
logit_bic = smf.logit('ST ~ ARA', data1999).fit()
print(logit_bic.summary())

# 类似前几章，结果和R不一样，还是用了和书上一样的
```

**NOTE**
> 这个函数只支持线性回归和Logistic回归，不支持Probit，所以这里没有再对Probit进行分析


## 7. 预测
[回到目录](#content)

### 7.1 预测
``` python
# 预测
# Logit全模型

predict_logit1 = logit1.predict(exog = data2000)
```

``` python
# 以0.50为阈值，查看预测结果

matrix_logit_1 = metrics.confusion_matrix(data2000['ST'], np.where(predict_logit1 > 0.5, 1, 0), labels=[0,1])
print(pd.DataFrame(matrix_logit_1))
```

``` python
# 以0为阈值，查看预测结果

matrix_logit_2 = metrics.confusion_matrix(data2000['ST'], np.where(predict_logit1 > 0, 1, 0), labels=[0,1])
print(pd.DataFrame(matrix_logit_2))
```

``` python
# 以0.05为阈值，查看预测结果

matrix_logit_3 = metrics.confusion_matrix(data2000['ST'], np.where(predict_logit1 > 0.05, 1, 0), labels=[0,1])
print(pd.DataFrame(matrix_logit_3))
```

### 7.2 ROC曲线

``` python
# 多个模型的ROC曲线，直接一起画了
# 四个模型：logit全模型，logit的AIC，logit的BIC，probit的全模型

# 计算预测值

predict_logit1 = logit1.predict(exog = data2000)
predict_logit_aic = logit_aic.predict(exog = data2000)
predict_logit_bic = logit_bic.predict(exog = data2000)
predict_probit1 = probit1.predict(exog = data2000)
```

``` python
# 计算fpr和tpr值

fpr_logit1, tpr_logit1, threshold_logit1 = metrics.roc_curve(data2000['ST'], predict_logit1, drop_intermediate=False)
fpr_logit_aic, tpr_logit_aic, threshold_logit_aic = metrics.roc_curve(data2000['ST'], predict_logit_aic, drop_intermediate=False)
fpr_logit_bic, tpr_logit_bic, threshold_logit_bic = metrics.roc_curve(data2000['ST'], predict_logit_bic, drop_intermediate=False)
fpr_probit1, tpr_probit1, threshold_probit1 = metrics.roc_curve(data2000['ST'], predict_probit1, drop_intermediate=False)
```

``` python
# 绘制ROC曲线

plt.figure()
plt.plot(fpr_logit1, tpr_logit1, color='red', label='logit1')
plt.plot(fpr_logit_aic, tpr_logit_aic, color='black', label='logit_aic')
plt.plot(fpr_logit_bic, tpr_logit_bic, color='orange', label='logit_bic')
plt.plot(fpr_probit1, tpr_probit1, color='green', label='probit1')
plt.plot([0, 1], [0, 1], color='blue', linestyle='--')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC curve')
plt.legend()  # 显示图例
plt.show()
```

**NOTE**
> 1. 结果和R的不完全一样，但是大概类似
> 2. 原因是阈值设定的不同，书上R的代码中是将0到1平均分成100份作为阈值，也就是0.01，0.02等等。
>而这里，是将预测值（就是predict的结果，即每个预测样本属于1的概率），降序排列，将每个概率值设为阈值。
 

## SUMMARY
[回到目录](#content)

>1. 这章没有什么新知识，所以也比较简单，注释也比较少。
>2. 主要就是调用`statsmodels`里面的不同模型

