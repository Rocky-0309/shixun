import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.bipartite import color
from sympy import rotations

# 创建x值数组（从-2到2，包含200个点）
x = np.linspace(-2, 2, 200)

# 计算对应的y值（y = x的立方）
y = x ** 3

# 创建图形和坐标轴
plt.figure(figsize=(8, 6))  # 设置图形大小

# 绘制曲线
plt.plot(x, y,
         label='$y = x^3$',  # 使用LaTeX格式的公式
         color='blue',        # 线条颜色
         linewidth=2)         # 线条粗细

# 添加标题和标签
plt.title('Cubic Function: $y = x^3$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend(loc='best')

# 设置坐标轴范围
plt.xlim(-2.2, 2.2)
plt.ylim(-8, 8)

# 添加坐标轴
plt.axhline(y=0, color='k', linewidth=0.8)  # x轴
plt.axvline(x=0, color='k', linewidth=0.8)  # y轴

# 高亮显示原点
plt.plot(0, 0, 'ro')  # 在(0,0)处画红色圆点
plt.annotate('Origin (0,0)',
             xy=(0, 0),
             xytext=(0.5, -1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# 显示图形
plt.tight_layout()  # 自动调整子图参数
plt.show()


year = np.arange(2000,2021).astype(np.str_)
month = np.random.randint(1,13,size = 20).astype(np.str_)
day = np.random.randint(1,31,size = 20).astype(np.str_)
date = np.array([])
for i in range(20):
    a = np.array([year[i],month[i],day[i]])
    b = ['/'.join(a)]
    date = np.append(date,b)

sales = np.random.randint(500,2000,size = len(date))

plt.xticks(range(0,len(date),2),['日期:%s'%i for i in date][::2],rotation = 45,color = 'red')
plt.plot(date,sales)

plt.show()