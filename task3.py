#练习题1
# 创建1-100的整数列表
numbers = [i for i in range(1, 101)]

# 使用列表推导式筛选偶数
even_numbers = [num for num in numbers if num % 2 == 0]

print("1-100之间的所有偶数：")
print(even_numbers)

#练习题2
def remove_duplicates(lst):
    """删除列表中的重复元素并保持原始顺序"""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 测试数据
original_list = [3, 2, 1, 2, 4, 3, 5, 4, 6, 5, 7]
unique_list = remove_duplicates(original_list)

print("\n原始列表:", original_list)
print("去重后的列表:", unique_list)

#练习题3
keys = ["a", "b", "c"]
values = [1, 2, 3]

# 使用zip函数和字典推导式合并两个列表
merged_dict = {k: v for k, v in zip(keys, values)}

print("\n合并后的字典:")
print(merged_dict)

#练习题4
# 定义一个学生信息的元组
student_info = ("张三", 20, 92.5)

# 解包元组
name, age, score = student_info

print("\n学生信息:")
print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")