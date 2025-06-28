# 练习题1
s1 = "Python is a powerful programming language"
s2 = " Let's learn together"

# (1) 提取单词 "language"
words = s1.split()
last_word = words[-1]
print("(1) 最后一个单词:", last_word)

# (2) 连接字符串并重复输出3次
combined = s1 + s2
print("\n(2) 连接后的字符串重复3次:")
print(combined * 3)

# (3) 输出所有以p或P开头的单词
p_words = [word for word in words if word.startswith('p') or word.startswith('P')]
print("\n(3) 以p或P开头的单词:", p_words)

# 练习题2
s3 = " Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
trimmed = s3.strip()
print("\n(1) 去除前后空格后的字符串:", f"'{trimmed}'")

# (2) 将所有字符转换为大写
uppercase = trimmed.upper()
print("(2) 转换为大写:", uppercase)

# (3) 查找子串 "test" 的起始下标
test_index = trimmed.find("test")
print("(3) 'test'的起始下标:", test_index)

# (4) 将 "test" 替换为 "practice"
replaced = trimmed.replace("test", "practice")
print("(4) 替换后的字符串:", replaced)

# (5) 分割字符串并用"-"连接
split_words = replaced.split()
joined = "-".join(split_words)
print("(5) 分割并连接后的字符串:", joined)