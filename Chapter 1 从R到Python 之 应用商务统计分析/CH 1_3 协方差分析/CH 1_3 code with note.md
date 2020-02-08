# Chapter 1_3 协方差分析

----
Author: W.Y.  
Date: 2020/1/15  
Update: 2020/2/4  
Info: 王汉生老师书的第三章，协方差分析的Python极简实现 

----

## CONTENT

1. [导入模块](#1-导入模块)  
2. [数据导入与预处理](#2-数据导入与预处理)
3. [描述性分析（画图）](#3-描述性分析画图)
4. [协方差分析](#4-协方差分析)
5. [模型诊断](#6-模型诊断)
6. [变量选择](#6-变量选择)
7. [预测](#7-预测)
8. [SUMMARY](#SUMMARY)

## 1. 导入模块
[回到目录](#content)

``` python
# 导入模块

import pandas as pd
import matplotlib.pyplot as plt  
import matplotlib
import seaborn as sns
import statsmodels.formula.api as smf  
import statsmodels.api as sma
import lmdiag  
import stepwiseSelection
```

## 2. 数据导入与预处理
[回到目录](#content)

``` python
# 导入数据

data = pd.read_csv('E:/Data Mining/SimplePython/Chapter 1 从R到Python/CH 1_3 协方差分析/CH 1_3 data teaching.csv', encoding='gbk')
```

``` python
# 预览数据

data.head()
```

## 3. 描述性分析（画图）
### 3.1 散点图

``` python
# 散点图

plt.scatter(data['size'], data['score'])  # 最简单的散点图，什么都不标注。其它设置可以看看第一章，这里就不重复了。
```

``` python
# 分成7组

bins = [0,20,40,60,80,100,120,140]
data['size_group'] = pd.cut(data['size'],bins)
```

``` python
# 频数分布

data['size_group'].value_counts(sort=False)
```

### 3.2 箱图

``` python
# 箱图

sns.boxplot(data['size_group'], data['score'])
```

``` python
# 赋值新变量

data['group'] = data['size'].apply(lambda x: 1 if x<=20 else 0)
```

**NOTE**
>1. `lambda`函数，Python中的匿名函数（Anonymous Function），具体请参考[番外]()。建议掌握，很实用。
>2. 这里的意思很好理解，就是：  
>2.1 如果值（x）小于等于20，则`data['group']`赋值为1，否则为0。  
>2.2 将这个规则应用于`data['size']`这列（`apply()`）

``` python
# 箱图

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus']=False  # 正常显示负号

fig = plt.figure(figsize=(8, 6))  # 设置画布大小
sns.boxplot(data['title'],data['score'], color='white', ax=plt.subplot(3,2,1)) 
sns.boxplot(data['gender'], data['score'], color='white', ax=plt.subplot(3,2,2))
sns.boxplot(data['student'],data['score'], color='white', ax=plt.subplot(3,2,3))
sns.boxplot(data['year'],data['score'], color='white',ax=plt.subplot(3,2,4))
sns.boxplot(data['semester'],data['score'], color='white',ax=plt.subplot(3,2,5))
sns.boxplot(data['group'],data['score'], color='white',ax=plt.subplot(3,2,6))
fig.tight_layout()
```


## 4. 协方差分析
[回到目录](#content)

### 4.1 单因素可加
``` python
# 协方差分析（其实本质还是回归）

model1 = smf.ols('score ~ C(group) + size',
                 data).fit()
print(model1.summary())
```

``` python
# 真实值和拟合值

plt.scatter(data['size'], data['score'])
plt.scatter(data['size'], model1.fittedvalues, c='red')
```

### 4.2 单因素交互
``` python
# 加入交互项

model2 = smf.ols('score ~ C(group)*size',
                 data).fit()
print(sma.stats.anova_lm(model2, typ=3))
```

``` python
print(model2.summary())
```

``` python
# 再次对真实值和拟合值画图

plt.scatter(data['size'], data['score'])
plt.scatter(data['size'], model2.fittedvalues, c='red')
```

### 4.3 多因素
``` python
# 全模型

model3a = smf.ols('score ~ C(title) + C(gender) + C(student) + '
                  'C(year) + C(semester) + C(group)*size', data).fit()
print(sma.stats.anova_lm(model3a, typ=3))
```

``` python
print(model3a.summary())
```

``` python
# 只保留显著的变量

model3b = smf.ols('score ~ C(title) + C(student) + '
                  'C(year) + C(group)*size', data).fit()
print(sma.stats.anova_lm(model3b, typ=3))
```

``` python
print(model3b.summary())
```

## 5. 模型诊断
[回到目录](#content)

``` python
# 模型诊断

lmdiag.plot(model3b)
```

``` python
# 查看模型的AIC和BIC值

print('AIC值：', model3b.aic,
      '\nBIC值：', model3b.bic)
```

**NOTE**
>计算结果和R不一样。已经在第一章提到过。我没解决，可以自己看看~


## 6. 变量选择
[回到目录](#content)

``` python
# 变量选择

X_train = pd.DataFrame(data, columns=['title', 'gender', 'student', 'year',
                                      'semester', 'group', 'size'])
X_train['group:size'] = X_train['group']*X_train['size']
```

**NOTE**
>1. 选择自变量列作为新的数据框。
>2. 因为只能选择已有自变量列，无法用交互项，所以只能手动相乘变成新变量

``` python
# AIC 

aic_vars, aic_logs = stepwiseSelection.backwardSelection(X_train, data['score'])
```

``` python
model_aic = smf.ols('score ~ C(title) + C(student) + '
                  'C(year) + C(group)*size', data).fit()
print(sma.stats.anova_lm(model_aic, typ=3))
```

``` python
# BIC

bic_vars, bic_logs = stepwiseSelection.backwardSelection(X_train, data['score'], elimination_criteria='bic')
```

``` python
model_bic = smf.ols('score ~ C(title) + C(student) + '
                  'C(year) + C(group)*size', data).fit()
print(sma.stats.anova_lm(model_bic, typ=3))

# 类似第一章,结果和R不同，为了后面结果的对比，我还是选择了和书上一样的变量。
```

## 7. 预测
[回到目录](#content)

``` python
# 预测

data_new = pd.read_csv('E:/Data Mining/SimplePython/Chapter 1 从R到Python/CH 1_3 协方差分析/CH 1_3 data new.csv', encoding='gbk')
```

``` python
data_new['group'] = data_new['size'].apply(lambda x: 1 if x<=20 else 0)
```

``` python
print(data_new)
```

``` python
# 残差

data['residual'] = model3b.resid
```

``` python
# 调整后的成绩

print(data.head())
```
## SUMMARY
[回到目录](#content)

>1. 这章没有什么新知识，所以也比较简单，注释也比较少。
>2. 主要有1点，可以自选掌握：  
>2.1  `lambda`函数，结合[番外]()学习

