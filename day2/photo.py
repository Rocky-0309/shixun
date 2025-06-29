import numpy as np
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

# 1. 读取TIFF文件
file_path = r"E:\shixun\day2\2020_0427_fire_B2348_B12_10m_roi\2020_0427_fire_B2348_B12_10m_roi.tif"
with rasterio.open(file_path) as src:
    # 读取所有波段数据（形状：[波段数, 高度, 宽度]）
    data = src.read()
    profile = src.profile  # 获取元数据

    # 确认波段信息
    print(f"波段数: {src.count}")
    print(f"波段顺序: {src.descriptions}")

# 2. 提取RGB波段（根据文件名推测）
# 文件名 'B2348_B12' 可能表示波段顺序：B2, B3, B4, B8, B12
# Sentinel-2 标准波段：
#   B2 = 蓝 (490 nm)
#   B3 = 绿 (560 nm)
#   B4 = 红 (665 nm)
blue_band = data[0]  # B2 (索引0)
green_band = data[1]  # B3 (索引1)
red_band = data[2]  # B4 (索引2)


# 3. 数据压缩 (0-10000 → 0-255)
def scale_to_255(band):
    band_min = band.min()
    band_max = band.max()
    # 线性缩放 + 转换为8位整数
    return ((band - band_min) / (band_max - band_min) * 255).astype(np.uint8)


red_scaled = scale_to_255(red_band)
green_scaled = scale_to_255(green_band)
blue_scaled = scale_to_255(blue_band)

# 4. 组合RGB三通道
rgb_image = np.dstack((red_scaled, green_scaled, blue_scaled))

# 5. 可视化结果
plt.figure(figsize=(12, 8))
plt.imshow(rgb_image)
plt.title('Sentinel-2 RGB Composite')
plt.axis('off')
plt.show()

# 6. 保存结果（可选）
output_path = r"E:\shixun\day2\2020_0427_fire_RGB.tif"
profile.update(
    count=3,  # RGB三波段
    dtype=rasterio.uint8
)

with rasterio.open(output_path, 'w', **profile) as dst:
    dst.write(red_scaled, 1)  # 红波段
    dst.write(green_scaled, 2)  # 绿波段
    dst.write(blue_scaled, 3)  # 蓝波段