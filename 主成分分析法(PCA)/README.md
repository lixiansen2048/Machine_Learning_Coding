# 主成分分析法

- 一个非监督的机器学习方法
- 主要用于数据的降维
- 通过降维可以发现更便于人类理解的特征
- 其他应用：可视化，去噪

目标：求w,使得 
<a href="https://www.codecogs.com/eqnedit.php?latex=f(X)&space;=&space;\frac{1}{m}\sum_{m}^{1}\left&space;(&space;X\cdot&space;w&space;\right&space;)^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(X)&space;=&space;\frac{1}{m}\sum_{m}^{1}\left&space;(&space;X\cdot&space;w&space;\right&space;)^{2}" title="f(X) = \frac{1}{m}\sum_{m}^{1}\left ( X\cdot w \right )^{2}" /></a> 最大

梯度：
<a href="https://www.codecogs.com/eqnedit.php?latex=\triangledown&space;f&space;=&space;\frac{2}{m}\cdot&space;X^{T}\left&space;(&space;X\cdot&space;w&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\triangledown&space;f&space;=&space;\frac{2}{m}\cdot&space;X^{T}\left&space;(&space;X\cdot&space;w&space;\right&space;)" title="\triangledown f = \frac{2}{m}\cdot X^{T}\left ( X\cdot w \right )" /></a>
