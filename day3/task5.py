import pandas as pd
import os
import numpy as np

# 设置文件路径
base_dir = r"E:\shixun\day3\exercise_data"
files = [
    os.path.join(base_dir, "2015年国内主要城市年度数据.csv"),
    os.path.join(base_dir, "2016年国内主要城市年度数据.csv"),
    os.path.join(base_dir, "2017年国内主要城市年度数据.csv")
]

# 1. 读取并纵向连接数据
dfs = []  # 存储各年份数据的列表

for file in files:
    # 读取CSV文件（使用utf-8-sig编码处理BOM头）
    df = pd.read_csv(file, encoding='utf-8-sig')

    # 从文件名提取年份
    year = os.path.basename(file)[:4]
    df['年份'] = int(year)  # 添加年份列

    dfs.append(df)

# 纵向连接所有数据
combined_df = pd.concat(dfs, axis=0, ignore_index=True)

# 2. 按年份聚合
# 3. 求每年的国内生产总值总和
yearly_gdp = combined_df.groupby('年份')['国内生产总值'].sum().reset_index()
yearly_gdp.columns = ['年份', '全国GDP(亿元)']

# 4. 处理缺省值，填充为0
combined_df_filled = combined_df.fillna(0)

# 5. 计算每个城市2015-2017年GDP的年均增长率，并找出增长率最高和最低的五个城市
# 创建城市GDP透视表
gdp_pivot = combined_df_filled.pivot_table(
    index='地区',
    columns='年份',
    values='国内生产总值'
).reset_index()

# 计算年均增长率 (2017年GDP/2015年GDP)^(1/2) - 1
gdp_pivot['年均增长率'] = (gdp_pivot[2017] / gdp_pivot[2015]) ** (1 / 2) - 1

# 排序并获取增长率最高和最低的5个城市
top5_growth = gdp_pivot.sort_values('年均增长率', ascending=False).head(5)
bottom5_growth = gdp_pivot.sort_values('年均增长率', ascending=True).head(5)


# 6. 对医院、卫生院数进行归一化处理（Min-Max标准化），并按年份比较各城市医疗资源的变化
# 按年份分组进行归一化
def min_max_normalize(group):
    min_val = group['医院、卫生院数'].min()
    max_val = group['医院、卫生院数'].max()
    # 避免除以零
    if max_val == min_val:
        group['归一化医疗资源'] = 0.5
    else:
        group['归一化医疗资源'] = (group['医院、卫生院数'] - min_val) / (max_val - min_val)
    return group


# 应用归一化
combined_df_normalized = combined_df_filled.groupby('年份').apply(min_max_normalize)

# 7. 提取北京、上海、广州、深圳四个城市2015-2017的GDP和社会商品零售总额数据
target_cities = ['北京', '上海', '广州', '深圳']
selected_cities_data = combined_df_filled[
    combined_df_filled['地区'].isin(target_cities)
][['地区', '年份', '国内生产总值', '社会商品零售总额']]

# 保存到新CSV文件
output_selected_path = os.path.join(base_dir, "一线城市GDP与社会商品零售总额.csv")
selected_cities_data.to_csv(output_selected_path, index=False, encoding='utf-8-sig')

# 打印结果
print("=" * 80)
print("纵向连接后的数据（前5行）:")
print(combined_df_filled.head())
print("\n" + "=" * 80)
print("按年份聚合的全国GDP:")
print(yearly_gdp)
print("\n" + "=" * 80)
print("GDP年均增长率最高的5个城市:")
print(top5_growth[['地区', 2015, 2017, '年均增长率']])
print("\n" + "=" * 80)
print("GDP年均增长率最低的5个城市:")
print(bottom5_growth[['地区', 2015, 2017, '年均增长率']])
print("\n" + "=" * 80)
print("医疗资源归一化结果（示例）:")
print(combined_df_normalized[['地区', '年份', '医院、卫生院数', '归一化医疗资源']].head(10))
print("\n" + "=" * 80)
print("四个一线城市GDP与社会商品零售数据已保存至:", output_selected_path)
print("=" * 80)