# 第四天实验日志

## 机器学习、深度学习以及实验环境配置
### 硬件环境
- GPU检查：`nvidia-smi`确认驱动版本>450
- 显存：根据GPU型号确认

### 软件环境
```bash
# 创建conda环境
conda create -n pytorch python=3.11
conda activate pytorch

# PyTorch安装（根据官网最新命令）
pip3 install torch torchvision torchaudio
```
### 实验数据集
#### 1. 鸢尾花数据集（分类任务）
- 样本量：150（3类各50）
- 特征：4个形态特征（花萼/花瓣长宽）
- 可视化代码：
```
plt.scatter(X_iris[:,2], X_iris[:,3], c=y_iris)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
```
#### 2. 合成回归数据集
- 样本量：100
- 特征：1维
- 噪声：标准差=10
- 可视化：线性散点图

# PyTorch 安装指南

## 1. 环境准备
### 系统要求
- Windows 10/11 | Linux | macOS 10.15+
- Python 3.8-3.11 (推荐3.9)
- pip ≥ 20.0

### GPU支持检查
```bash
nvidia-smi  # 查看CUDA版本（需≥11.7）
```

### 通过pip安装
```commandline
conda install pytorch==2.3.8 torchvision==0.18.0 torchaudi0==2.3.0 pytorch-cuda=11.8-p
```
### 验证安装
```commandline
import torch

print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
print(f"GPU数量: {torch.cuda.device_count()}")
print(f"当前GPU: {torch.cuda.current_device()}")
print(f"设备名称: {torch.cuda.get_device_name(0)}")
```