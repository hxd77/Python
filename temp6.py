import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import platform

# -----------------------------------------------------------
#  通用数据提取函数
# -----------------------------------------------------------
def get_time_series(df, indicators):
    mask = df['指标'].isin(indicators)
    sub_df = df[mask].copy()
    sub_df.set_index('指标', inplace=True)
    sub_df = sub_df.T
    sub_df = sub_df.iloc[::-1] 
    return sub_df

def plot_patent_quality(file_path):
    # 字体设置
    system_name = platform.system()
    if system_name == "Windows":
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
    elif system_name == "Darwin":
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC']
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 读取数据
    df = None
    encodings = ['gb18030', 'gbk', 'utf-8-sig', 'utf-8']
    for enc in encodings:
        try:
            df = pd.read_csv(file_path, skiprows=2, encoding=enc, engine='python')
            cols_str = "".join([str(c) for c in df.columns])
            if '指标' in cols_str or '年' in cols_str:
                break
        except:
            continue
            
    if df is None:
        print("无法读取文件")
        return
    
    # 清洗列名
    df.columns = df.columns.str.strip()
    if '指标' not in df.columns:
         potential = [c for c in df.columns if '指标' in str(c)]
         if potential: df.rename(columns={potential[0]: '指标'}, inplace=True)

    # 提取数据：专利申请数 和 发明专利申请数
    indicators = {
        'total': '专利申请数(项)',
        'invention': '发明专利申请数(项)'
    }
    
    df_plot = get_time_series(df, list(indicators.values()))
    
    # 清洗年份
    df_plot.index = df_plot.index.astype(str).str.replace('年', '', regex=False)
    df_plot = df_plot[df_plot.index.str.isnumeric()]
    df_plot.index = df_plot.index.astype(int)
    
    # 过滤年份 (只保留2015-2023)
    df_plot = df_plot[df_plot.index <= 2023]
    df_plot = df_plot.sort_index()

    # 转数值
    for col in df_plot.columns:
        df_plot[col] = pd.to_numeric(df_plot[col], errors='coerce')
    
    s_total = df_plot.get(indicators['total'])
    s_invention = df_plot.get(indicators['invention'])
    years = df_plot.index
    
    # 计算发明专利占比 (衡量质量的指标)
    invention_ratio = (s_invention / s_total) * 100

    # ==========================================
    # 绘图：双轴图 (柱状图=总量, 折线图=占比)
    # ==========================================
    fig, ax1 = plt.subplots(figsize=(12, 7))
    width = 0.6
    
    # 左轴：专利申请总数 (柱状图)
    # 转换单位为 "万项" 以简化坐标轴
    p1 = ax1.bar(years, s_total / 10000, width, label='专利申请总数 (万项)', color='#a6cee3', alpha=0.9, zorder=10)
    
    # 右轴：发明专利占比 (折线图)
    ax2 = ax1.twinx()
    p2 = ax2.plot(years, invention_ratio, color='#e31a1c', linewidth=3, marker='D', markersize=8, label='发明专利占比 (%)', zorder=20)
    
    # -----------------------------------------------------------
    # 美化与标注
    # -----------------------------------------------------------
    ax1.set_title('图五：科技产出质量分析——专利申请规模与发明专利占比 (2015-2023)', fontsize=15, fontweight='bold', pad=20)
    ax1.set_xlabel('年份', fontsize=12)
    ax1.set_ylabel('专利申请数 (万项)', fontsize=12, color='#333')
    ax2.set_ylabel('发明专利占比 (含金量 %)', fontsize=12, color='#e31a1c', fontweight='bold')
    
    # 格式化
    ax2.yaxis.set_major_formatter(ticker.PercentFormatter(decimals=1))
    ax2.tick_params(axis='y', labelcolor='#e31a1c')
    ax1.grid(True, axis='y', linestyle='--', alpha=0.3)
    
    # 标注最新年份的数据
    last_year = years.max()
    last_val_bar = s_total[last_year] / 10000
    last_val_line = invention_ratio[last_year]
    
    ax1.text(last_year, last_val_bar, f'{last_val_bar:.0f}', ha='center', va='bottom', fontsize=10)
    ax2.text(last_year, last_val_line, f'{last_val_line:.1f}%', ha='center', va='bottom', color='#e31a1c', fontweight='bold', xytext=(0,8), textcoords='offset points')

    # 合并图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.tight_layout()
    plt.savefig('patent_quality_analysis.png', dpi=300)
    print("已保存图五: patent_quality_analysis.png")
    plt.show()

if __name__ == "__main__":
    plot_patent_quality('data.csv')