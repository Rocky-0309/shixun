# Python数据分析与网络爬虫实验总结

## 一、核心技术栈掌握
- **Pandas**：数据处理与分析
- **Requests**：网页爬取
- **lxml**：数据解析（XPath）
- **Matplotlib**：数据可视化

## 二、Pandas核心技能
### 数据结构构建
- 从字典/列表/NumPy数组创建Series和DataFrame
- 数据合并：`merge()` 和 `concat()` 
- 分组统计：`groupby()`

### 关键操作
```python
df.head()/info()/describe()  # 数据预览
df.loc[]/iloc[]             # 索引选择
df.fillna()/dropna()        # 缺失值处理
```

## 三、网络爬虫技术实践
### Requests库应用
- 设置Headers模拟浏览器访问
- 突破反爬机制（User-Agent）
- 网页源码保存技术

### lxml数据解析
```python
# XPath核心技巧
tree.xpath('标签路径')          # 节点定位
tree.xpath('//div/@属性')       # 属性提取
tree.xpath('div[contains(@class,"value")]') # 条件过滤
```

## 四、Matplotlib可视化基础
### 核心操作流程
```
plt.figure()             # 创建图形对象
plt.plot(x, y)           # 绘制数据
plt.title('标题')        # 添加标题
plt.legend()             # 添加图例
plt.show()               # 显示图形
```
## 五、典型问题与解决方案
### 典型问题
- 豆瓣返回403状态码
- 电影名称乱码字符
- 数据合并出现NaN值
### 解决方案
- 添加User-Agent请求头
- replace()+strip()组合清洗
- 左连接保留原始数据 + 填充策略
