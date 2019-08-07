# 线性回归算法总结

- 典型的参数学习
对比KNN：非参数学习

- 只能解决回归问题
很多分类方法中，线性回归是基础（如逻辑回归）
对比KNN，既能解决分类问题，又能解决回归问题


- 对数据有假设：线性
对比KNN，对数据没有假设


-优点：对数据具有强解释性

## 多元线性回归的正规方程解(Normal Equation):

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\huge&space;$$&space;\theta&space;=&space;(X_b^TX_b)^-^1X_b^Ty&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\huge&space;$$&space;\theta&space;=&space;(X_b^TX_b)^-^1X_b^Ty&space;$$" title="\huge $$ \theta = (X_b^TX_b)^-^1X_b^Ty $$" /></a>

问题：时间复杂度高

## 梯度下降法

- 不是一个机器学习算法
- 是一种基于搜索的最优化方法
- 作用：最小化一个损失函数
- 梯度上升法：最大化一个效用函数