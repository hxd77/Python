import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# ==========================================
# 1. 基础设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 定义颜色
COLOR_LEFT = '#95A5A6'   # 2016年 (灰色，代表过去)
COLOR_RIGHT = '#E74C3C'  # 2023年 (红色，代表现在)

# ==========================================
# 2. 读取与清洗数据
# ==========================================
filename = "data.csv"
print(f"正在读取文件: {filename} ...")

try:
    df = pd.read_csv(filename, encoding='GB18030', skiprows=2)
except:
    try:
        df = pd.read_excel(filename, skiprows=2)
    except Exception as e:
        print(f"读取失败: {e}")
        sys.exit(1)

# 数据清洗函数
def get_clean_data(df, indicators):
    mask = df['指标'].isin(indicators)
    sub_df = df[mask].copy()
    if sub_df.empty: return pd.DataFrame()
    sub_df.set_index('指标', inplace=True)
    sub_df = sub_df.T
    sub_df = sub_df.iloc[::-1] # 倒序
    try:
        sub_df.index = sub_df.index.str.replace('年', '').astype(int)
    except:
        sub_df.index = sub_df.index.astype(str).str.extract(r'(\d+)')[0].astype(int)
    return sub_df.apply(pd.to_numeric, errors='coerce')

# ==========================================
# 3. 准备数据
# ==========================================
raw_indicators = [
    '发表科技论文(万篇)', 
    '科技成果登记数(项)', 
    '专利申请数(项)', 
    '发明专利申请数(项)', 
    '专利申请授权数(项)', 
    '发明专利申请授权数(项)',
    '国家技术发明奖(项)',
    '国家科学技术进步奖(项)'
]

df_funnel = get_clean_data(df, raw_indicators)

# 数据处理
df_funnel['国家奖项(项)'] = df_funnel['国家技术发明奖(项)'].fillna(0) + df_funnel['国家科学技术进步奖(项)'].fillna(0)
df_funnel['发表科技论文(篇)'] = df_funnel['发表科技论文(万篇)'] * 10000

# 漏斗步骤
funnel_steps = [
    '发表科技论文(篇)', 
    '科技成果登记数(项)', 
    '专利申请数(项)', 
    '发明专利申请数(项)', 
    '专利申请授权数(项)', 
    '发明专利申请授权数(项)',
    '国家奖项(项)'
]

step_labels = [
    '发表科技论文', '科技成果登记', '专利申请总数', 
    '发明专利申请', '专利授权总数', '发明专利授权', '国家级奖项'
]

# 选取对比年份 (2016 vs 2023)
# 2016年通常数据比较全，2015有时会有缺失，您可以根据实际情况改
year_left = 2016
year_right = 2023

# 检查数据是否存在
if year_left not in df_funnel.index or year_right not in df_funnel.index:
    print(f"错误: 缺少 {year_left} 或 {year_right} 的数据。")
    # 自动寻找最早和最晚的完整年份
    valid_years = df_funnel[funnel_steps].dropna().index
    year_left = valid_years.min()
    year_right = valid_years.max()
    print(f"自动调整为: {year_left} vs {year_right}")

values_left = df_funnel.loc[year_left, funnel_steps].fillna(0).values
values_right = df_funnel.loc[year_right, funnel_steps].fillna(0).values

# ==========================================
# 4. 绘制蝴蝶图 (Butterfly Chart)
# ==========================================
fig, ax = plt.subplots(figsize=(14, 8))

y_pos = np.arange(len(funnel_steps))
bar_height = 0.6

# 左侧条形 (负值)
bars_left = ax.barh(y_pos, -values_left, height=bar_height, align='center', 
                    color=COLOR_LEFT, alpha=0.8, label=f'{year_left}年')

# 右侧条形 (正值)
bars_right = ax.barh(y_pos, values_right, height=bar_height, align='center', 
                     color=COLOR_RIGHT, alpha=0.8, label=f'{year_right}年')

# --- 装饰图表 ---
ax.set_yticks(y_pos)
ax.set_yticklabels([]) # 隐藏默认Y轴标签，我们手动画在中间
ax.set_title(f'中国科技创新能力演变：蝴蝶图对比 ({year_left} vs {year_right})', 
             fontsize=18, fontweight='bold', pad=20)
ax.legend(loc='upper right')

# 隐藏边框
for spine in ax.spines.values():
    spine.set_visible(False)
# 隐藏X轴刻度 (因为左右数量级可能不同，主要看形状，或者看标注)
ax.set_xticks([])

# --- 添加标签和数值 ---

# 1. 中间标签列
for i, label in enumerate(step_labels):
    ax.text(0, i, label, ha='center', va='center', 
            fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# 2. 左侧数值
for bar, value in zip(bars_left, values_left):
    width = bar.get_width() # width 是正数
    # 格式化
    if value > 10000: val_str = f"{value/10000:.1f}万"
    else: val_str = f"{int(value)}"
    
    ax.text(-width - (np.max(values_right)*0.05), bar.get_y() + bar.get_height()/2, 
            val_str, ha='right', va='center', fontsize=10, color=COLOR_LEFT, fontweight='bold')

# 3. 右侧数值
for bar, value in zip(bars_right, values_right):
    width = bar.get_width()
    if value > 10000: val_str = f"{value/10000:.1f}万"
    else: val_str = f"{int(value)}"
    
    ax.text(width + (np.max(values_right)*0.05), bar.get_y() + bar.get_height()/2, 
            val_str, ha='left', va='center', fontsize=10, color=COLOR_RIGHT, fontweight='bold')

# 添加增长率提示 (针对发明专利)
idx_inv = 3 # 发明专利申请在第4个位置 (index 3)
growth = ((values_right[idx_inv] - values_left[idx_inv]) / values_left[idx_inv]) * 100
ax.text(values_right[idx_inv] * 1.3, idx_inv, f"↑增长{growth:.0f}%", 
        color='red', fontsize=10, ha='left', va='center', fontweight='bold')

# 底部水印
ax.text(0.5, -0.05, '注：左侧为历史数据，右侧为最新数据；中心轴为各指标名称', 
        transform=ax.transAxes, ha='center', fontsize=10, color='gray')

plt.tight_layout()
plt.savefig('Innovation_Butterfly_Chart.png', dpi=150)
print("图表已生成: Innovation_Butterfly_Chart.png")
plt.show()