### Softmax

#### Softmax的形式
Sigmoid 单输出节点是确定概率值，Softmax 输出节点的输出值是概率分布。

#### Softmax 为何加指数函数？
1. 指数函数的曲线斜率逐渐增大，能够将输出值拉开距离。
2. 指数函数在反向传播求梯度求导的时候比较方便。
3. 当输出值非常大，指数值可能会溢出，所有输出值都减去max(输出值) 来优化。

#### Softmax 求导
$$
\mathcal{Softmax}(z_i) = \frac{e^{z_i}}{\Sigma_{c=1}^C e^{z_c}}
$$
i 是输出节点编号，设 $\hat{y}_i = \frac{e^{z_i}}{\Sigma_{c=1}^C e^{z_c}} = p_i$，则
1. $i \neq j$
$$
\begin{align}
\frac{\partial \hat{y}_i}{\partial z_j} &= \frac{0 - e^{z_i}
e^{z_j}}{(\Sigma_{c=1}^C e^{z_c})^2} \\
&= -\frac{e^{z_i}}{\Sigma_{c=1}^C e^{z_c}} \frac{e^{z_j}}{\Sigma_{c=1}^C
e^{z_c}} \\
&= - p_i p_j
\end{align}
$$

2. $i = j$
$$
\begin{align}
\frac{\partial \hat{y}_i}{\partial z_j} &= \frac{e^{z_i} \Sigma_{c=1}^C e^{z_c}
- e^{z_i} e^{z_j}}{(\Sigma_{c=1}^C e^{z_c})^2} \\
&= \frac{e^{z_i} (\Sigma_{c=1}^C e^{z_c} - e^{z_j})}{(\Sigma_{c=1}^C e^{z_c})^2}
\\
&= \frac{e^{z_i}}{\Sigma_{c=1}^C e^{z_c}} \frac{\Sigma_{c=1}^C e^{z_c} -
e^{z_j}}{\Sigma_{c=1}^C e^{z_c}} \\
&= p_i (1 - p_j) \\
&= p_i - p_i^2
\end{align}
$$

#### 交叉熵损失函数
Softmax 是输出节点的激活函数，交叉熵是损失函数。

###### 溢出
Softmax 计算输出值容易溢出，交叉熵也容易溢出，一般统一实现。

Softmax 分子分母同时乘以非零常数E，等式不变，
$$\hat{y}_i = \frac{e^{z_i}}{\Sigma_{c=1}^C e^{z_c}} = \frac{E e^{z_i}}{E
\Sigma_{c=1}^C e^{z_c}} = \frac{e^{z_i + log(E)}}{\Sigma_{c=1}^C e^{z_c +
log(E)}}
$$

让所有的 $z_i + log(E)$在0附近，最好小于零，所以用max没用mean，令 $log(E) = - max(z_1, z_2, ...,
z_C)$，可以有效防止溢出。

###### 损失函数
一般使用最大似然估计（Maximum likelihood estimation）来构造损失函数。

p是模型预测的概率值，y是类标签，二分类问题：

$$L = P(y|x) = (p)^y (1-p)^{1-y}$$

多分类问题：

$$L = P(y|x) = \prod_{i=1}^{C} p_i^{y_i}$$

连乘结果容易为0，连加求导方便，用log transformation，似然函数取对数的负数，最小化对数似然函数，

$$\operatorname*{arg\ min} L = - log P(y|x) = -\Sigma_{i=1}^{C} y_i log p_i$$

标准交叉熵形式中只针对正确类别的输出节点计算，
$$\operatorname*{arg\ min} L = -log p_i$$

Softmax 取对数加负号，得到交叉熵，跟标准交叉熵形式等价。
$$- log p_i = - log(\frac{e^{z_i}}{\Sigma_{c=1}^C e^{z_c}})
$$

#### References
[1] [一文详解Softmax函数](https://zhuanlan.zhihu.com/p/105722023)
