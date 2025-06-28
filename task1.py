# 练习题1: 判断变量类型
x = 10
y = "10"
z = True
print(f"x 的类型是: {type(x)}")   # <class 'int'>
print(f"y 的类型是: {type(y)}")   # <class 'str'>
print(f"z 的类型是: {type(z)}\n") # <class 'bool'>

# 练习题2: 计算圆面积
radius = float(input("请输入圆的半径: "))
pi = 3.14
area = pi * radius ** 2
print(f"圆的面积为: {area:.2f}\n")  # 保留两位小数

# 练习题3: 类型转换观察
num_str = "3.14"
num_float = float(num_str)  # 字符串转浮点数
num_int = int(num_float)    # 浮点数转整数
print(f"原始字符串: {num_str} (类型: {type(num_str)})")
print(f"转浮点数后: {num_float} (类型: {type(num_float)})")
print(f"再转整数后: {num_int} (类型: {type(num_int)})")