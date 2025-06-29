# 练习题1
def is_palindrome(num):
    """判断一个数是否为回文数"""
    num_str = str(num)
    return num_str == num_str[::-1]

# 测试
print(f"121 是回文数吗? {is_palindrome(121)}")  # True
print(f"123 是回文数吗? {is_palindrome(123)}")  # False
print(f"12321 是回文数吗? {is_palindrome(12321)}")  # True

# 练习题2
def calculate_average(*args):
    """计算任意数量参数的平均值"""
    if len(args) == 0:
        return 0  # 避免除以零错误
    return sum(args) / len(args)

# 测试
print(f"1, 2, 3 的平均值: {calculate_average(1, 2, 3):.2f}")  # 2.00
print(f"10, 20, 30, 40 的平均值: {calculate_average(10, 20, 30, 40):.2f}")  # 25.00

# 练习题3
def find_longest_string(*strings):
    """返回任意多个字符串中最长的一个"""
    if not strings:
        return None  # 如果没有参数，返回None
    return max(strings, key=len)

# 测试
result = find_longest_string("apple", "banana", "cherry", "date")
print(f"最长的字符串是: {result}")  # banana
result = find_longest_string("Python", "Java", "C++", "JavaScript")
print(f"最长的字符串是: {result}")  # JavaScript

# 练习题4-1
# 矩形计算模块

def area(length, width):
    """计算矩形面积"""
    return length * width

def perimeter(length, width):
    """计算矩形周长"""
    return 2 * (length + width)