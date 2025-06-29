# Python 学习笔记：函数、NumPy 与 Markdown
## 函数与模块
### 函数定义关键要素
#### 参数处理：

*位置参数与关键字参数的灵活运用

*使用 *args 和 **kwargs 处理可变参数

*类型注解提升代码可读性： def process(data: list[str]) -> int:

#### 函数：

*闭包函数（closure）实现状态保持

*Lambda 表达式创建匿名函数

*装饰器扩展函数功能
## NumPy 科学计算
### 核心功能实践
```
import numpy as np

# 创建矩阵
matrix = np.array([[1, 2], [3, 4]], dtype=np.float32)

# 广播机制实现高效运算
result = matrix * 5  # 标量与矩阵运算

# 布尔索引筛选数据
filtered_data = matrix[matrix > 2]

# 矩阵拼接
new_matrix = np.vstack((matrix, [5, 6]))
```
### 数据持久化
```
# 保存为二进制格式
np.save("matrix.npy", matrix)

# 加载数据
loaded_data = np.load("matrix.npy")
```
## Markdown 文档规范
### 核心语法应用
```
## 二级标题（标题层级）

### 代码块嵌入
```python
print("Hello World")  # Python 代码示例
```
