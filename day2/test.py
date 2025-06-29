# 使用矩形计算模块
from task5 import area, perimeter

# 输入矩形尺寸
l = float(input("请输入矩形的长度: "))
w = float(input("请输入矩形的宽度: "))

# 计算并输出结果
print(f"矩形面积: {area(l, w):.2f}")
print(f"矩形周长: {perimeter(l, w):.2f}")