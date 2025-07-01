import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 国家列表
countries = ['挪威', '德国', '中国', '美国', '瑞典']
# 金牌个数 (NumPy数组)
gold_medal = np.array([16, 12, 9, 8, 8])
# 银牌个数 (NumPy数组)
silver_medal = np.array([8, 10, 4, 10, 5])
# 铜牌个数 (普通列表)
bronze_medal = [13, 5, 2, 7, 5]

# 创建坐标位置
x = np.arange(len(countries))

# 设置图表
plt.figure(figsize=(10, 6))
# 设置x轴刻度标签
plt.xticks(x, countries)
# 绘制分组柱状图
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold", label='金牌')
plt.bar(x, silver_medal, width=0.2, color="silver", label='银牌')
plt.bar(x + 0.2, bronze_medal, width=0.2, color="#CD7F32", label='铜牌')  # 使用铜牌标准色

# 添加数据标签
# 金牌标签
for i in range(len(x)):
    plt.text(x[i] - 0.2, gold_medal[i], str(gold_medal[i]),
             va='bottom', ha='center', fontsize=8)
# 银牌标签
for i in range(len(x)):
    plt.text(x[i], silver_medal[i], str(silver_medal[i]),
             va='bottom', ha='center', fontsize=8)
# 铜牌标签
for i in range(len(x)):
    plt.text(x[i] + 0.2, bronze_medal[i], str(bronze_medal[i]),
             va='bottom', ha='center', fontsize=8)

# 添加图例和标题
plt.legend()
plt.title('2022北京冬奥会奖牌榜TOP5', fontsize=14)
plt.xlabel('国家', fontsize=12)
plt.ylabel('奖牌数量', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 显示图表
plt.tight_layout()
plt.show()