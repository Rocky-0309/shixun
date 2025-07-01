import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取CSV文件
file_path = "E:/shixun/day3/exercise_data/train.csv"
titanic = pd.read_csv(file_path)

# 1. 性别对生还率的影响
gender_survival = titanic.groupby('Sex')['Survived'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Sex', y='Survived', data=gender_survival,
            palette='viridis', hue='Sex', legend=False)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. 年龄对生还率的影响
# 创建年龄分组并计算生还率
titanic['AgeGroup'] = pd.cut(titanic['Age'],
                             bins=[0, 12, 18, 30, 50, 80],
                             labels=['Child (<12)', 'Teen (12-18)',
                                     'Young Adult (19-30)',
                                     'Adult (31-50)', 'Senior (51+)'])

# 显式设置 observed=False 以避免警告
age_survival = titanic.groupby('AgeGroup', observed=False)['Survived'].mean().reset_index()

plt.figure(figsize=(12, 7))
sns.barplot(x='AgeGroup', y='Survived', data=age_survival,
            palette='coolwarm', hue='AgeGroup', legend=False)
plt.title('Survival Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 3. 性别和年龄组合分析
plt.figure(figsize=(14, 8))
sns.barplot(x='AgeGroup', y='Survived', hue='Sex',
            data=titanic, palette='Set2', errorbar=None)
plt.title('Survival Rate by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.legend(title='Gender', loc='upper right')
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()