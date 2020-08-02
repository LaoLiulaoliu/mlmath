线性回归的推导，数学解释

Input: $$
X =
  \begin{bmatrix}
  1 & 2 & \cdots & 3\\
  4 & 4 & \cdots & 6\\
  7 & 8 & \cdots & 9\\
  \vdots & \vdots & \ddots & \vdots \\
  11 & 12& \cdots & 13\\
  \end{bmatrix}_{m*n}
,
Y =
  \begin{bmatrix}
  9\\
  11\\
  13\\
  \vdots\\
  19\\
  \end{bmatrix}_{m*1}
$$

$$ $$

Hypothesis: $$ H_\theta(x) = \sum\limits_{i=0}^n \theta_i x_i $$

Loss Function: $$ L(\theta) = \sum\limits_{j=0}^m \frac{1}{2m} (H_\theta(x)^j -
y^j)^2 $$

Partial Derivative for every $\theta$: $$ \frac{\partial L(\theta)}{\partial
\theta_i} = \frac{1}{m} \sum\limits_{j=0}^m (H_\theta(x)^j - y^j) x_i^j $$

Gradient descent optimization of $\theta$: $$ \theta_i = \theta_i - \frac{1}{m}
\sum\limits_{j=0}^m (H_\theta(x)^j - y^j) x_i^j $$

在实际线性回归拟合中，对于Input，m代表数据量，n代表要拟合出的方程系数，一般$m \gg n$。

当我们把线性回归拟合看作解方程组时，要求解的未知数$\theta$有n个，就不严谨的认为一共有 n行 n个方程组成了方程组。行列式
$\begin{vmatrix} X \end{vmatrix}_{n*n} \neq 0$，根据克莱姆法则，方程组有唯一解。

从矩阵的角度看，非齐次线性方程组 X$\theta =
Y$，系数矩阵X的秩等于增广矩阵$\overline{X}$（即$\begin{pmatrix}XY\end{pmatrix}$），$r(X)=r(\overline{X})=n$，方程组有唯一解，$\begin{vmatrix}
X \end{vmatrix}_{n*n}
$是非奇异方阵。如果$r(X)=r(\overline{X})=r<n$，方程组有无穷多组解，就是我们说的可能优化到局部最优点。

从n维空间中的向量角度看，$X_1,X_2,...,X_n$
线性无关，且是极大线性无关组，是一组基，则向量组X的秩（也是列秩）$r(X)=n$。$r(X)<n$，则方程有很多局部最有点。极大线性无关组不唯一，有几个极大线性无关组，就有几个全局最优解。
