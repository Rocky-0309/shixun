import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 读取数据
df_2015 = pd.read_csv('E:/shixun/day3/exercise_data/2015年国内主要城市年度数据.csv')
df_2016 = pd.read_csv('E:/shixun/day3/exercise_data/2016年国内主要城市年度数据.csv')
df_2017 = pd.read_csv('E:/shixun/day3/exercise_data/2017年国内主要城市年度数据.csv')

# 创建画布
plt.figure(figsize=(16, 10))

# 1. 2015-2017年GDP直方图
plt.subplot(2, 1, 1)  # 2行1列的第1个位置

# 合并三年的数据
df_2015['年份'] = 2015
df_2016['年份'] = 2016
df_2017['年份'] = 2017

# 合并数据
df_all = pd.concat([df_2015, df_2016, df_2017])

# 只取前15个城市以避免图表过于拥挤
cities = df_2015.sort_values('国内生产总值', ascending=False).head(15)['地区'].tolist()
df_top15 = df_all[df_all['地区'].isin(cities)]

# 创建柱状图位置
x = np.arange(len(cities))  # 城市位置
width = 0.25  # 柱宽

# 绘制柱状图
for i, year in enumerate([2015, 2016, 2017]):
    year_data = df_top15[df_top15['年份'] == year]
    # 确保数据顺序一致
    sorted_data = year_data.set_index('地区').reindex(cities)['国内生产总值']
    plt.bar(x + i*width, sorted_data, width=width,
            label=f'{year}年', alpha=0.8)

# 添加标签和标题
plt.title('2015-2017年主要城市GDP对比（前15名）', fontsize=16)
plt.xlabel('城市', fontsize=12)
plt.ylabel('GDP（亿元）', fontsize=12)
plt.xticks(x + width, cities, rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加数据标签
for i, city in enumerate(cities):
    for j, year in enumerate([2015, 2016, 2017]):
        gdp = df_top15[(df_top15['地区'] == city) &
                      (df_top15['年份'] == year)]['国内生产总值'].values[0]
        plt.text(i + j*width, gdp + 100, f'{gdp:.0f}',
                ha='center', va='bottom', fontsize=8, rotation=0)

# 2. 2015年GDP饼状图
plt.subplot(2, 2, 3)  # 2行2列的第3个位置

# 按GDP降序排序
df_2015_sorted = df_2015.sort_values('国内生产总值', ascending=False)

# 取前5名城市，其他城市合并为"其他"
top5 = df_2015_sorted.head(5)
other_sum = df_2015_sorted.iloc[5:]['国内生产总值'].sum()

# 创建饼图数据
labels = list(top5['地区']) + ['其他']
sizes = list(top5['国内生产总值']) + [other_sum]

# 设置颜色
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'violet', 'silver']

# 绘制饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90, shadow=True, explode=(0.1, 0, 0, 0, 0, 0))
plt.title('2015年主要城市GDP占比（前5名）', fontsize=14)
plt.axis('equal')  # 确保饼图是圆形

# 3. 添加2015年GDP排名前10城市柱状图
plt.subplot(2, 2, 4)  # 2行2列的第4个位置

# 取GDP前10的城市
top10 = df_2015_sorted.head(10)

# 绘制柱状图
plt.barh(top10['地区'], top10['国内生产总值'], color='teal')
plt.title('2015年GDP排名前10城市', fontsize=14)
plt.xlabel('GDP（亿元）', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 添加数据标签
for i, v in enumerate(top10['国内生产总值']):
    plt.text(v + 100, i, f'{v:.0f}', va='center', fontsize=9)

# 调整布局
plt.tight_layout()
plt.savefig('城市GDP分析.png', dpi=300, bbox_inches='tight')
plt.show()