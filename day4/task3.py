import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
file_path = "E:\\shixun\\day3\\exercise_data\\train.csv"
data = pd.read_csv(file_path)

# 计算每个等级的总人数和生还人数
survival_by_class = data.groupby('Pclass')['Survived'].agg(
    Total='count',
    Survived='sum'
)

# 计算生还率
survival_by_class['Survival Rate'] = (survival_by_class['Survived'] / survival_by_class['Total']) * 100

# 重置索引以便绘图
survival_by_class = survival_by_class.reset_index()

# 创建直方图
plt.figure(figsize=(10, 6))
bars = plt.bar(
    survival_by_class['Pclass'].astype(str),  # 将等级转为字符串类型
    survival_by_class['Survival Rate'],
    color=['#1f77b4', '#ff7f0e', '#2ca02c'],  # 为不同等级设置不同颜色
    width=0.6
)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f'{height:.1f}%',
        ha='center',
        va='bottom',
        fontsize=12
    )

# 添加标题和标签
plt.title('Survival Rate by Passenger Class', fontsize=14)
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.ylim(0, 100)  # 设置Y轴范围

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 显示图表
plt.tight_layout()
plt.show()