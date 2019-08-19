# 主成分分析法

- 一个非监督的机器学习方法
- 主要用于数据的降维
- 通过降维可以发现更便于人类理解的特征
- 其他应用：可视化，去噪

目标：求w,使得 f(X) = \frac{1}{m}\sum_{m}^{1}\left ( X\cdot w \right )^{2} 最大

梯度：
\triangledown f = \frac{2}{m}\cdot X^{T}\left ( X\cdot w \right )
