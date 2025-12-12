import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# ==========================================
# 1. 基础设置与配色
# ==========================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 定义漏斗颜色 (从冷色到暖色，代表筛选过程)
# 颜色顺序：浅蓝 -> 深蓝 -> 紫色 -> 深紫 -> 红 -> 深红 -> 金色
FUNNEL_COLORS = [
    '#AED6F1', # 论文 (海量)
    '#5DADE2', # 成果
    '#48C9B0', # 专利申请
    '#1ABC9C', # 发明申请 (核心)
    '#F1948A', # 专利授权
    '#E74C3C', # 发明授权 (通过)
    '#F1C40F'  # 国家奖项 (皇冠)
]

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
# 3. 提取漏斗所需的指标
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

# 【关键处理 1】合并“国家奖项” 
df_funnel['国家奖项(项)'] = df_funnel['国家技术发明奖(项)'].fillna(0) + df_funnel['国家科学技术进步奖(项)'].fillna(0)

# 【关键处理 2】单位换算 (万篇 -> 篇)
# 必须统一单位，否则论文数(几百)和专利数(几百万)没法画在一种图上
df_funnel['发表科技论文(篇)'] = df_funnel['发表科技论文(万篇)'] * 10000

# 定义最终的漏斗顺序 (逻辑顺序)
funnel_steps = [
    '发表科技论文(篇)', 
    '科技成果登记数(项)', 
    '专利申请数(项)', 
    '发明专利申请数(项)', 
    '专利申请授权数(项)', 
    '发明专利申请授权数(项)',
    '国家奖项(项)'
]

# 简化显示的标签
step_labels = [
    '发表科技论文', 
    '科技成果登记', 
    '专利申请总数', 
    '发明专利申请', 
    '专利授权总数', 
    '发明专利授权', 
    '国家级奖项'
]

# ==========================================
# 4. 选取最新年份数据
# ==========================================
# 自动寻找这些指标都不为空的最新年份
valid_df = df_funnel[funnel_steps].dropna()

if valid_df.empty:
    print("错误: 找不到所有指标都齐全的年份。尝试放宽条件...")
    # 如果找不到齐全的，就用最新的一年，缺少的填0
    target_year = df_funnel.index.max()
    print(f"使用最新年份: {target_year} (部分数据可能缺失)")
    values = df_funnel.loc[target_year, funnel_steps].fillna(0).values
else:
    target_year = valid_df.index.max()
    print(f"使用数据最全的年份: {target_year}")
    values = valid_df.loc[target_year, funnel_steps].values

# ==========================================
# 5. 绘制居中漏斗图
# ==========================================
fig, ax = plt.subplots(figsize=(12, 8))

# 倒序数据，让第一步(论文)在最上面
y_pos = np.arange(len(funnel_steps))[::-1] 

# 计算居中绘图的参数
# trick: 使用 barh，但是让左边缘(left)等于 -value/2，这样 bar 就会以 x=0 为中心
left_pos = -values / 2

# 绘制柱状图
bars = ax.barh(y_pos, values, left=left_pos, height=0.6, 
               color=FUNNEL_COLORS, edgecolor='white', alpha=0.9)

# --- 装饰图表 ---
# 隐藏坐标轴，只保留图形
ax.axis('off')

# 添加标题
ax.set_title(f'中国科技创新转化漏斗 ({target_year}年)\n从科研产出到国家荣誉的筛选路径', 
             fontsize=18, fontweight='bold', pad=20)

# 添加标签和数值
for i, (bar, label, value) in enumerate(zip(bars, step_labels, values)):
    # 1. 在左侧标注 阶段名称
    ax.text(-np.max(values)/1.6, bar.get_y() + bar.get_height()/2, label, 
            ha='right', va='center', fontsize=12, fontweight='bold', color='#333')
    
    # 2. 在中间标注 具体数值
    # 格式化数值：如果超过1万，用"万"作单位，否则直接显示
    if value > 10000:
        val_str = f"{value/10000:.1f}万"
    else:
        val_str = f"{int(value)}"
        
    ax.text(0, bar.get_y() + bar.get_height()/2, val_str, 
            ha='center', va='center', fontsize=11, color='white' if i>2 else 'black', fontweight='bold')
    
    # 3. 在右侧标注 转化率 (相对于上一级的比例)
    # 第一级不标转化率
    if i > 0:
        prev_value = values[i-1]
        # 防止除以0
        if prev_value > 0:
            rate = (value / prev_value) * 100
            # 画虚线连接
            ax.plot([values[i-1]/2, values[i]/2], [y_pos[i-1], y_pos[i]], 'k--', alpha=0.1)
            
            ax.text(np.max(values)/1.6, bar.get_y() + bar.get_height()/2, 
                    f"转化率: {rate:.1f}%", 
                    ha='left', va='center', fontsize=10, color='gray')

# 添加右下角水印
ax.text(0.95, 0.05, '注：科技论文已换算为"篇"以统一单位', 
        transform=ax.transAxes, ha='right', fontsize=10, color='gray')

plt.tight_layout()
plt.savefig('Innovation_Funnel_Chart.png', dpi=150)
print("图表已生成: Innovation_Funnel_Chart.png")
plt.show()