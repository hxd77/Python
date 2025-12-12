import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# ==========================================
# 1. 基础设置
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 读取数据
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

# --- 数据组 A: 进出口贸易 ---
trade_indicators = [
    '高技术产品出口额(亿美元)', 
    '高技术产品进口额(亿美元)'
]
df_trade = get_clean_data(df, trade_indicators).dropna()
years_trade = df_trade.index

# --- 数据组 B: 雷达图综合实力 (选取6个最具代表性的维度) ---
radar_indicators = [
    '研究与试验发展经费支出(亿元)',       # 投入 - 钱
    '研究与试验发展人员全时当量(万人年)', # 投入 - 人
    '发表科技论文(万篇)',                 # 产出 - 理论
    '发明专利申请数(项)',                 # 产出 - 技术
    '高技术产品出口额(亿美元)',           # 产出 - 国际贸易
    '技术市场成交额(亿元)'                # 产出 - 商业转化
]

# 简化雷达图标签 (去掉单位，避免拥挤)
radar_labels = ['R&D经费', 'R&D人员', '科技论文', '发明专利', '高技术出口', '技术成交额']

df_radar = get_clean_data(df, radar_indicators)
# 只对比最早(2015)和最新(通常是2023，因为2024部分数据缺失)
# 找到数据最全的最新年份
valid_years = df_radar.dropna().index
if len(valid_years) < 2:
    print("数据不足以绘制雷达对比图")
    sys.exit(1)

year_start = valid_years.min() # 2015
year_end = valid_years.max()   # 2023

# 提取这两年的数据
values_start = df_radar.loc[year_start].values
values_end = df_radar.loc[year_end].values

# 【关键步骤】数据归一化 (Normalization)
# 因为经费是几万亿，论文是几万篇，单位不同不能直接画。
# 我们把最新年份(2023)作为 100% (或者1.0)，计算2015年相对于2023年的比例。
# 这样雷达图的形状才好看。
max_values = np.maximum(values_start, values_end) # 取两者中的最大值做分母
# 防止分母为0
max_values[max_values == 0] = 1 

values_start_norm = values_start / max_values
values_end_norm = values_end / max_values

# ==========================================
# 4. 绘图
# ==========================================
fig = plt.figure(figsize=(14, 7))

# --- 图 1: 高技术产品进出口顺差图 (Area Chart) ---
ax1 = fig.add_subplot(1, 2, 1)

exports = df_trade['高技术产品出口额(亿美元)']
imports = df_trade['高技术产品进口额(亿美元)']

# 画线
ax1.plot(years_trade, exports, color='#E74C3C', linewidth=2, label='出口额 (卖钱)')
ax1.plot(years_trade, imports, color='#3498DB', linewidth=2, label='进口额 (花钱)')

# 填充区域 (ACCENT - Clarity: 顺差一目了然)
ax1.fill_between(years_trade, exports, imports, 
                 where=(exports >= imports), 
                 interpolate=True, color='#E74C3C', alpha=0.1, label='贸易顺差')
ax1.fill_between(years_trade, exports, imports, 
                 where=(exports < imports), 
                 interpolate=True, color='#3498DB', alpha=0.1, label='贸易逆差')

ax1.set_title('中国高技术产品国际竞争力 (进出口)', fontsize=14, fontweight='bold')
ax1.set_ylabel('金额 (亿美元)', fontsize=12)
ax1.set_xlabel('年份', fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.3)


# --- 图 2: 科技综合实力雷达图 (Radar Chart) ---
ax2 = fig.add_subplot(1, 2, 2, polar=True) # 极坐标系

# 闭合曲线 (把第一个点追加到最后)
angles = np.linspace(0, 2*np.pi, len(radar_labels), endpoint=False).tolist()
angles += angles[:1] # 闭合角度

values_start_plot = np.concatenate((values_start_norm, [values_start_norm[0]]))
values_end_plot = np.concatenate((values_end_norm, [values_end_norm[0]]))

# 画图
# 2015年 (起始)
ax2.plot(angles, values_start_plot, 'o-', linewidth=2, color='#95A5A6', label=f'{year_start}年')
ax2.fill(angles, values_start_plot, color='#95A5A6', alpha=0.25)

# 2023年 (最新)
ax2.plot(angles, values_end_plot, 'o-', linewidth=2, color='#2ECC71', label=f'{year_end}年')
ax2.fill(angles, values_end_plot, color='#2ECC71', alpha=0.15)

# 装饰雷达图
ax2.set_thetagrids(np.degrees(angles[:-1]), radar_labels, fontsize=11)
ax2.set_title(f'科技综合实力全维对比 ({year_start} vs {year_end})', fontsize=14, fontweight='bold', pad=20)
ax2.set_ylim(0, 1.1) # 范围 0 到 110%
ax2.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax2.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], color='gray', fontsize=8)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig('Tech_Trade_and_Radar.png', dpi=150)
print("图表已生成: Tech_Trade_and_Radar.png")
plt.show()