# Chapter 1_1 线性回归

----
author: W.Y.  
first_edition: 2019/12/31  
last_edition: 2020/1/18  
description: 王汉生老师书的第一章，线性回归的python极简实现  

----

## 导入模块

```
import pandas as pd  # NOTE。pandas模块用于读取数据、处理数据等
from numpy import mean, median, var, std  # 从模块numpy导入子模块；均值、中位数、方差、标准差
import matplotlib.pyplot as plt  # 画图模块
import matplotlib
import statsmodels.formula.api as smf  # 基于公式的统计模型API接口
import lmdiag  # 画模型诊断图的模块
from patsy import dmatrices  # NOTE。用于分析统计模型，构建矩阵（这里是为了做共线性诊断）
from statsmodels.stats.outliers_influence import variance_inflation_factor   # 用于共线性诊断
```

**NOTE**
>1. 导入pandas,命名为pd。通常在模块名很长时使用 import xxx as x的格式，方便简单。
>常用缩写有`import pandas as pd`, `import numpy as np`
>2. `from patsy import dmatrices`这句可能会出现`Cannot find reference`的报错，下面画红色波浪线，这算是Pycharm的bug吧，可以不管，可以正常运行


## 导入数据

```
# 导入数据之导入txt文件  
# NOTE
data = pd.read_csv('E:\Data Mining\SimplePython\Chapter 1 从R到Python\CH 1_1 线性回归\CH 1_1 data.txt', sep = '\s+')
```

**NOTE**
>1. 导入txt文件，常用函数有`read_csv()`, `read_table()`，主要区别是前者默认读取逗号分隔符，可指定其它分隔符，后者无默认分隔符，必须指定分隔符。
>2. 本案例的txt文件有些特殊，以多个空格分隔，且首行和其它行分隔的空格数不同，因此用正则表达式，`\s`代表空格、tab等空白字符，`\s+`代表多个空白字符 
>3. 表示路径时，理论上用`\`或者`/`都可以，但是我更建议用`/`，因为`\`也用做转义，如果文件名开头以数字或某些特殊单词开头时会出错。如果用`\`最好用`\\`
>4. 通常不建议用带有中文的路径，不管是R还是Python都是如此。不过这里我乐意~~


```
# 查看数据前10行。
# NOTE
data.head(10)
```
```
pd.DataFrame.head(data,10)
```

**NOTE**

>1. 可以看看R和Python`head()`函数的差别。
>2. `data.head(10)`和`pd.DataFrame.head(data, 10)`是一样的，都是调用了pandas模块中DataFrame这个类下面的head函数。
>python中很多函数都有这两种用法，通常会用第一种。
>3. 直接用`dataframe.head()`会输出前5行，加入数字则是相应的行，比如`dataframe.head(10)`就输出前10行。

拓展
>那么为什么不输入数字就默认输出5行呢？  
>可以用`ctrl+鼠标左键点击`函数，可以看到`def head(self, n=5):`这一句源代码，也就是说函数的参数默认值是5.  
>这里是拓展知识，之后写自定义函数的时候会用到，这里想到了就简单提一下~


```
# 数据分割，2002年用来建模，2003年用来预测
# NOTE
data2002 = data[data['year'] == 2002]
data2003 = data[data['year'] == 2003]
```

**NOTE**
>用pandas选择数据框中的列时，用`dataframe['column_name']`，就类似R中的`dataframe$col`


## 描述性分析（描述性统计）

```
# 描述性分析，单独计算
mean_ROEt = mean(data2002['ROEt'])  # 均值
median_ATO = median(data2002['ATO'])  # 中位数
var_PM = var(data2002['PM'])  # 方差
min_LEV = min(data2002['LEV'])  # 最小值
max_GROWTH = max(data2002['GROWTH'])  # 最大值
std_PB = std(data2002['PB'])

# NOTE
print('mean_ROEt:', mean_ROEt, 
      '\nmedian_ATO:', median_ATO,
      '\nvar_PM:', var_PM,
      '\nmin_LEV:', min_LEV,
      '\nmax_GROWTH:', max_GROWTH,
      '\nstd_PB:', std_PB) 
```

**NOTE**
>`print()`函数的用法，除了变量，其它要输出的都要用引号；输出要换行需要加入`\n`，代码中的换行只是为了好看


```
# 描述性分析，统一计算
# NOTE
df_describe = pd.concat([data2002.min(), data2002.max(),
                         data2002.median(), data2002.mean(),
                         data2002.var(), data2002.std()], axis=1)
df_describe.columns = ['min', 'max', 'median', 'mean', 'var', 'std']  # 重命名列名
df_describe.head()
```

**NOTE**
>`pd.concat()`是pandas模块下的`concat()`函数，用于合并数据框。其中`axis=1`是按列合并的意思，默认或者`axis=0`则是按行合并的意思。


## 描述性分析（画图）

```
# 散点图
# 绘制散点图
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 为了画图能够显示中文，否则中文会变成乱码。
plt.rcParams['axes.unicode_minus']=False  # 画图正常显示负号

plt.scatter(x = data2002.ROEt, # 指定散点图的x轴数据
            y = data2002.ROE, # 指定散点图的y轴数据
            s = 10,  # 指定散点图点的大小
            c = 'steelblue') # 指定散点图中点的颜色
# 添加x轴和y轴标签
plt.xlabel('ROEt')
plt.ylabel('ROE')
# 添加标题
plt.title('ROE和ROEt的散点图')
# 显示图形
plt.show()
```

## 相关分析

```
# NOTE
data.corr()
```

**NOTE**

> `data.corr()`和`data.head()`这样的写法只会输出结果，不会保存结果。
>如果，比如说要保存相关系数的结果，则用`result = data.corr()`这样的写法，然后再用`result`或者`print(result)`查看即可。

## 线性回归模型

```
# 一元线性回归 （x = ROEt, y = ROE）
# NOTE
model1 = smf.ols("ROE ~ ROEt", 
            data2002).fit()
print(model1.summary())
```

**NOTE**
> `smf.ols()`是用了`import statsmodels.formula.api as smf`之后，调用这个模块下的`ols()`函数。
>如果你设置的缩写是其它的，那么调用时就要用自己设置的缩写。
>或者如果没有设置缩写，就要用全名调用。这也是为什么会设置缩写，更加简洁。

```
# 多元线性回归 （x = ROEt+ATO+PM+LEV+GROWTH+PB+ARR+INV+ASSET, y = ROE）
model2 = smf.ols("ROE ~ ROEt + ATO + PM + LEV + GROWTH + PB + ARR + INV + ASSET", 
            data2002).fit()
model2.summary()  
#  请品一品用print()和没用print()的区别
```

## 模型诊断(画图)

```
lmdiag.plot(model2)
```

# 也可以单独画图
```
lmdiag.resid_fit(model2)  
```
```
lmdiag.q_q(model2)
```
```
lmdiag.scale_loc(model2)
```
```
lmdiag.resid_lev(model2)
```


**NOTE**
>细心的小伙伴应该发现了，Python画出的图，标出的异常值点和书上用R画图标出的点不同。
>比如书上的异常点是第**47**个，而Python画图显示第**46**个。那么这是为什么呢？  
>
>因为Python的Index是从0开始的。也就是说我们在R或者Excel里面的第1行，在Python里面就是第0行。
>

## 异常值删除
```
# 参考书上，删除第46个值
# NOTE
data2002_a = data2002.drop([46])
```

**NOTE**
>这里是用pandas删除行，删除了第46行。  
>如果是删除列，可以用`dataframe.drop(['column_name'], axis=1)`

```
# 再次回归
model3 = smf.ols("ROE ~ ROEt + ATO + PM + LEV + GROWTH + PB + ARR + INV + ASSET", 
            data2002_a).fit()
print(model3.summary()) 
```
```
# 再次诊断
lmdiag.plot(model3)
```

## 共线性诊断

```
# NOTE
y, X = dmatrices( 'ROE ~ ROEt + ATO + PM + LEV + GROWTH + PB + ARR + INV + ASSET', 
                  data = data2002_a, return_type= 'dataframe')

vif = pd.DataFrame()  # 构造空的数据框
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["variables"] = X.columns
vif
```

**NOTE**

>1. 看到这里用了双引号和单引号，python里面双引号和单引号功能是一样的，几乎没啥区别。
>在转义时有一点点区别。比如`print("let's go")`和`print('let\'s go')`是一样的，但是`print('let's go')`是会报错的。
>
>2. 这里可以看到R里面共线性就`vif(model)`就搞定，Python里还挺复杂。也可能是我没找到更好更简洁的代码哈。


**NOTE**  
以下两步暂时省略，有时间再补。  
1.变量选择 AIC  
2.变量选择 BIC

原因有二：
>1.跑这个python代码比R代码复杂很多，建议还是用R处理吧！  
>2.我自己也没跑过，不熟悉，没有找到AIC或BIC做逐步回归的模块，需要自己写函数。
>有需要请自行百度吧~或者之后我再补下。


## 预测
用基于2002年数据建立的模型预测2003年的数据

```
# 预测值
true = data2003['ROE']
predict1 = model3.predict(data2003)
```

```
# 误差值= 真实值-预测值
resid0 = true - data2003['ROEt']
resid1 = true - predict1
```
```
# 求平均误差（误差的均值）
# NOTE
resid_result = abs(pd.DataFrame(list(zip(resid0, resid1)))) 
resid_result.mean()
```

**NOTE**
>1. `abs()`函数，求绝对值
>2. `pd.DataFrame(list(zip(series1, series2)))`将Series(数组)转为DataFrame(数据框)。


**SUMMARY**

>1. 没啥好说的，这章很简单，其实很多代码和R有异曲同工之妙的。
>2. 主要有几点：  
>2.1 安装、导入相关的模块  
>2.2 一些基本函数的用法  
>2.3 利用pandas读取数据（本章是txt文件）  
>2.4 数据框（`pd.Dataframe`）的基本用法，做描述性统计等等  
>2.5 利用matplotlib画图
