import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import platform

def plot_rd_activity_structure(file_path):
    # -----------------------------------------------------------
    # 1. 字体与环境设置
    # -----------------------------------------------------------
    system_name = platform.system()
    if system_name == "Windows":
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
    elif system_name == "Darwin":
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC']
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # -----------------------------------------------------------
    # 2. 数据读取 (带错误处理)
    # -----------------------------------------------------------
    df = None
    encodings = ['gb18030', 'gbk', 'utf-8']
    for enc in encodings:
        try:
            df = pd.read_csv(file_path, skiprows=2, encoding=enc, engine='python')
            break
        except:
            continue
            
    if df is None:
        print("无法读取文件")
        return

    # -----------------------------------------------------------
    # 3. 数据清洗与提取
    # -----------------------------------------------------------
    # 定义 R&D 活动的三种类型
    indicators = {
        'basic': '研究与试验发展基础研究经费支出(亿元)',
        'applied': '研究与试验发展应用研究经费支出(亿元)',
        'dev': '研究与试验发展试验发展经费支出(亿元)'
    }
    
    # 提取数据
    df_plot = df[df['指标'].isin(indicators.values())].set_index('指标').T
    
    # 清洗索引
    df_plot.index = df_plot.index.astype(str).str.replace('年', '', regex=False)
    df_plot = df_plot[df_plot.index.str.isnumeric()] # 过滤非年份行
    df_plot.index = df_plot.index.astype(int)
    df_plot = df_plot.sort_index()
    
    # 转数值
    for col in df_plot.columns:
        df_plot[col] = pd.to_numeric(df_plot[col], errors='coerce')
        
    # 获取三列数据
    s_basic = df_plot.get(indicators['basic'])
    s_applied = df_plot.get(indicators['applied'])
    s_dev = df_plot.get(indicators['dev'])
    
    # -----------------------------------------------------------
    # 4. 绘图：堆叠柱状图 (Stacked Bar)
    # -----------------------------------------------------------
    fig, ax = plt.subplots(figsize=(12, 7))
    years = df_plot.index
    bar_width = 0.6
    
    # 绘制堆叠柱
    # 1. 底部：基础研究 (深色，强调根基)
    p1 = ax.bar(years, s_basic, width=bar_width, label='基础研究 (Basic Research)', color='#1f77b4', zorder=10)
    
    # 2. 中间：应用研究 (中间色)
    p2 = ax.bar(years, s_applied, width=bar_width, bottom=s_basic, 
                label='应用研究 (Applied Research)', color='#2ca02c', zorder=10)
    
    # 3. 顶部：试验发展 (浅色/亮色，占比最大)
    # bottom = basic + applied
    p3 = ax.bar(years, s_dev, width=bar_width, bottom=s_basic + s_applied, 
                label='试验发展 (Experimental Dev.)', color='#ff7f0e', zorder=10)

    # -----------------------------------------------------------
    # 5. 添加高分细节：基础研究占比折线
    # -----------------------------------------------------------
    # 在很多分析中，"基础研究占比"是衡量创新质量的核心指标
    # 我们用双轴把这个比例画出来，体现图表的深度
    
    total = s_basic + s_applied + s_dev
    basic_ratio = (s_basic / total) * 100
    
    ax2 = ax.twinx()
    p_line = ax2.plot(years, basic_ratio, color='#d62728', linewidth=2.5, 
                      marker='o', markersize=8, label='基础研究占比 (%)', zorder=20)
    
    # -----------------------------------------------------------
    # 6. 图表美化
    # -----------------------------------------------------------
    ax.set_title('R&D经费支出结构：基础研究 vs 应用研究 vs 试验发展', fontsize=16, pad=20, fontweight='bold')
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('经费支出 (亿元)', fontsize=12, color='#333')
    ax2.set_ylabel('基础研究投入占比 (%)', fontsize=12, color='#d62728', fontweight='bold')
    
    # 设置刻度格式
    ax2.yaxis.set_major_formatter(ticker.PercentFormatter(decimals=1))
    ax2.tick_params(axis='y', labelcolor='#d62728')
    
    # 添加数值标签（只在最新的年份添加，避免乱）
    last_year = years.max()
    last_basic_pct = basic_ratio[last_year]
    ax2.annotate(f'{last_basic_pct:.2f}%', 
                 xy=(last_year, last_basic_pct), 
                 xytext=(0, 10), textcoords='offset points', 
                 ha='center', color='#d62728', fontweight='bold')

    # 合并图例
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    # 放在图表外部或上方，避免遮挡
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

    ax.grid(True, axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    
    output_file = 'rd_internal_structure.png'
    plt.savefig(output_file, dpi=300)
    print(f"图表已保存: {output_file}")
    plt.show()

if __name__ == "__main__":
    file_path = "data.csv"
    plot_rd_activity_structure(file_path)