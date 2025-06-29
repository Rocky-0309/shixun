import os
import re
import locale


def natural_sort_key(s):
    """
    自然排序键函数，用于模仿Windows资源管理器的排序方式
    """
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', s)]


# 设置路径
image_folder = r"E:\shixun\day2\作业\新建文件夹"
txt_file_path = r"E:\shixun\day2\作业\新建文本文档.txt"

# 设置系统区域设置，确保排序结果与系统一致
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass  # 如果区域设置失败，继续使用默认设置

# 读取文本文件中的新文件名
with open(txt_file_path, 'r', encoding='utf-8') as f:
    new_names = [line.strip() for line in f.readlines() if line.strip()]

# 获取文件夹中的所有图片文件（支持常见格式）
image_files = [f for f in os.listdir(image_folder)
               if os.path.isfile(os.path.join(image_folder, f))
               and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]

# 按照Windows资源管理器的自然排序顺序排序
image_files.sort(key=natural_sort_key)

print("检测到的图片文件顺序（按照Windows资源管理器排序）：")
for i, f in enumerate(image_files, 1):
    print(f"{i}. {f}")

# 检查文件数量是否匹配
if len(image_files) != len(new_names):
    print(f"\n警告: 图片文件数量({len(image_files)})与文本行数({len(new_names)})不匹配！")
    print("将只重命名匹配的文件")

# 批量重命名
success_count = 0
for i, (old_name, new_name) in enumerate(zip(image_files, new_names)):
    # 获取文件扩展名
    _, ext = os.path.splitext(old_name)

    # 构造完整路径
    old_path = os.path.join(image_folder, old_name)
    new_path = os.path.join(image_folder, f"{new_name}{ext}")

    # 执行重命名
    try:
        # 检查新文件名是否已存在
        if os.path.exists(new_path):
            print(f"警告: 文件名 '{new_name}{ext}' 已存在，跳过重命名")
            continue

        os.rename(old_path, new_path)
        print(f"重命名成功: {old_name} -> {new_name}{ext}")
        success_count += 1
    except Exception as e:
        print(f"重命名失败: {old_name} -> {new_name}{ext} | 错误: {str(e)}")

print(f"\n操作完成! 成功重命名 {success_count}/{len(image_files)} 个文件")