# 主成分分析法

- 一个非监督的机器学习方法
- 主要用于数据的降维
- 通过降维可以发现更便于人类理解的特征
- 其他应用：可视化，去噪

目标：求w,使得 
<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;f(X)&space;=&space;\frac{1}{m}\sum_{m}^{1}\left&space;(&space;X\cdot&space;w&space;\right&space;)^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;f(X)&space;=&space;\frac{1}{m}\sum_{m}^{1}\left&space;(&space;X\cdot&space;w&space;\right&space;)^{2}" title="\large f(X) = \frac{1}{m}\sum_{m}^{1}\left ( X\cdot w \right )^{2}" /></a>最大

梯度：
<a href="https://www.codecogs.com/eqnedit.php?latex=\triangledown&space;f&space;=&space;\frac{2}{m}\cdot&space;X^{T}\left&space;(&space;X\cdot&space;w&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\triangledown&space;f&space;=&space;\frac{2}{m}\cdot&space;X^{T}\left&space;(&space;X\cdot&space;w&space;\right&space;)" title="\triangledown f = \frac{2}{m}\cdot X^{T}\left ( X\cdot w \right )" /></a>


## 偏差与方差

- 有一些算法天生是高方差的算法，如KNN
- 非参数学习通常都是高方差算法。因为不对数据进行任何假设
- 有一些算法天生是高偏差算法，如线性回归
- 参数学习通常都是高偏差算法，因为对数据具有极强的假设

**不过**：
大多数算法具有相应的参数，可以调整偏差和方差
如 KNN 中的 K,线性回归中使用多项式回归

**关系**：
+ 偏差与方差通常是矛盾的
+ 降低偏差会提高方差
+ 降低方差会提高偏差

**机器学习的主要挑战来自于方差**

**解决高方差的通常手段**：
1. 降低模型复杂度
2. 减少数据维度；降噪
3. 增加样本数
4. 使用验证集

# 模型正则化
## 岭回归
目标：使
<img src="https://latex.codecogs.com/gif.latex?\LARGE&space;J(\theta&space;)&space;=&space;MSE(y,\hat{y};\theta&space;)&space;&plus;&space;\alpha&space;\frac{1}{2}\sum_{1}^{n}\theta&space;_{i}^{2}" title="\LARGE J(\theta ) = MSE(y,\hat{y};\theta ) + \alpha \frac{1}{2}\sum_{1}^{n}\theta _{i}^{2}" />
尽可能小

## LASSO 回归
目标：使
<img src="https://latex.codecogs.com/gif.latex?\LARGE&space;J(\theta&space;)&space;=&space;MSE(y,\hat{y};\theta&space;)&space;&plus;&space;\alpha&space;\sum_{1}^{n}\left&space;|&space;\theta&space;\right&space;|" title="\LARGE J(\theta ) = MSE(y,\hat{y};\theta ) + \alpha \sum_{1}^{n}\left | \theta \right |" />
尽可能小