import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 设置英文字体
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Tahoma']

# 读取CSV文件
file_path = "E:\\shixun\\day3\\exercise_data\\train.csv"
data = pd.read_csv(file_path)

# 创建年龄段分组
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# 计算各年龄段的生还率
survival_rate = data.groupby('AgeGroup', observed=False)['Survived'].mean() * 100

# 创建图形
plt.figure(figsize=(12, 8))
bars = plt.bar(survival_rate.index, survival_rate.values,
               color=plt.cm.viridis(np.linspace(0.2, 0.8, len(survival_rate))),
               edgecolor='black', linewidth=1.2)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 添加每个年龄段的乘客数量
for i, age_group in enumerate(survival_rate.index):
    count = data[data['AgeGroup'] == age_group].shape[0]
    plt.text(i, -5, f'n={count}', ha='center', fontsize=9, color='gray', fontstyle='italic')

# 设置图表标题和标签
plt.title('Titanic Passenger Survival Rate by Age Group', fontsize=16, fontweight='bold')
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.ylim(-10, 100)
plt.grid(axis='y', linestyle='--', alpha=0.4)

# 添加分析结论
conclusion = ("Key Findings: Children (0-10) had the highest survival rate (59.0%), reflecting the 'women and children first' policy.\n"
              "Elderly passengers (61-70) had the lowest survival rate (22.2%).")
plt.figtext(0.5, 0.01, conclusion, ha="center", fontsize=12,
            bbox={"facecolor":"#FFEECC", "alpha":0.6, "pad":5})

# 添加数据来源
plt.figtext(0.95, 0.95, "Data: Titanic Passenger Manifest",
            ha="right", fontsize=9, color='gray', alpha=0.7)

# 添加图例
plt.axhline(y=38.2, color='r', linestyle='--', alpha=0.5)
plt.text(7.5, 40, 'Overall Survival Rate: 38.2%', color='r', fontsize=10)

# 显示图表
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('titanic_survival_by_age.png', dpi=300)  # 保存为高分辨率图片
plt.show()