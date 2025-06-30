import pandas as pd
import numpy as np
import os

# 设置文件保存路径
base_dir = r"E:\shixun\day3\exercise_data"

# 1. 创建包含指定数据的DataFrame
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['张三', '李四', '王五', np.nan, '赵六', '钱七'],
    'Score': [88.5, 92.0, 76.5, 85.0, np.nan, 95.5],
    'Grade': ['A', 'A', 'B', 'B', 'A', 'A+']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 2. 保存为CSV文件
original_path = os.path.join(base_dir, "students.csv")
df.to_csv(original_path, index=False, encoding='utf-8-sig')
print(f"原始数据已保存至: {original_path}")
print("原始数据内容:")
print(df)
print("\n" + "="*80)

# 3. 读取CSV文件
df_read = pd.read_csv(original_path)

# 打印前3行
print("读取文件的前3行:")
print(df_read.head(3))
print("\n" + "="*80)

# 4. 处理缺失值
# 计算Score的平均分（排除NaN）
score_mean = df_read['Score'].mean()

# 填充缺失值
df_cleaned = df_read.copy()
df_cleaned['Score'].fillna(score_mean, inplace=True)
df_cleaned['Name'].fillna('Unknown', inplace=True)

# 打印处理后的数据
print("处理后的数据:")
print(df_cleaned)
print("\n" + "="*80)
print(f"Score平均值: {score_mean:.2f}")
print("\n" + "="*80)

# 5. 保存为新的CSV文件
cleaned_path = os.path.join(base_dir, "students_cleaned.csv")
df_cleaned.to_csv(cleaned_path, index=False, encoding='utf-8-sig')
print(f"清理后的数据已保存至: {cleaned_path}")