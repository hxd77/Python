import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# === 1. 设置中文字体 (防止乱码) ===
# 尝试设置常用中文字体，如果系统中没有这些字体，可能需要手动指定路径
system_fonts = ['SimHei', 'Microsoft YaHei', 'Heiti TC', 'sans-serif']
mpl.rcParams['font.sans-serif'] = system_fonts
mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# === 2. 数据准备 ===
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']

# 进出口数据 (亿美元) - 2024年数据为 None
exports = [6552.12, 6035.73, 6674.44, 7468.16, 7307.14, 7762.55, 9749.0, 9467.0, 8420.0, None]
imports = [5480.58, 5236.21, 5840.34, 6716.61, 6377.91, 6821.01, 8342.0, 7606.0, 6799.0, None]

# 转换 None 为 np.nan 以便绘图时自动留空
exports = [np.nan if x is None else x for x in exports]
imports = [np.nan if x is None else x for x in imports]

# 技术市场成交额 (亿元)
turnover = [9835.79, 11406.98, 13424.22, 17697.42, 22398.39, 28251.51, 37294.3, 47791.02, 61475.66, 68354.0]

# === 3. 创建图表 ===
fig, ax1 = plt.subplots(figsize=(12, 7))

# 设置柱状图宽度
bar_width = 0.5

# --- 绘制左轴 (进出口堆叠柱状图) ---
# 绘制出口 (下方蓝色)
p1 = ax1.bar(years, exports, width=bar_width, label='出口额 (Export)', color='#3b82f6', alpha=0.9)
# 绘制进口 (上方紫色)，bottom 参数设置为 exports 的值以实现堆叠
p2 = ax1.bar(years, imports, width=bar_width, bottom=exports, label='进口额 (Import)', color='#8b5cf6', alpha=0.9)

# 设置左轴标签和范围
ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('进出口额 (亿美元)', color='#333333', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#333333')

# --- 绘制右轴 (技术市场成交额折线图) ---
ax2 = ax1.twinx()  # 共享 X 轴

# 绘制折线
p3 = ax2.plot(years, turnover, color='#dc2626', label='技术市场成交额', linewidth=3, marker='o', markersize=6, markerfacecolor='white', markeredgewidth=2)

# 设置右轴标签
ax2.set_ylabel('技术市场成交额 (亿元)', color='#dc2626', fontsize=12, fontweight='bold', rotation=270, labelpad=20)
ax2.tick_params(axis='y', labelcolor='#dc2626')

# === 4. 图表美化 ===
plt.title('高技术产品贸易与技术市场发展趋势 (2015-2024)', fontsize=16, pad=20)

# 网格线 (仅显示左轴的水平网格)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# --- 合并图例 ---
# 由于使用了双轴，自动图例需要手动合并 handles 和 labels
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
# 将柱状图放在图例前面，折线图放在后面
ax2.legend(lines + lines2, labels + labels2, loc='upper left', frameon=True, shadow=True)

# 添加数值标签 (可选)
# 给折线图添加数值
for i, v in enumerate(turnover):
    ax2.text(i, v + 2000, f'{int(v)}', ha='center', va='bottom', color='#dc2626', fontsize=9, fontweight='bold')

# 调整布局防止标签截断
plt.tight_layout()

# 显示图表
plt.show()