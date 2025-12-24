import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import platform

def plot_tech_stats(file_path):
    """
    读取数据并绘制高技术产品进出口与技术市场成交额的双轴复合图。
    """
    
    # -----------------------------------------------------------
    # 1. 设置中文字体 (根据不同操作系统尝试加载常用中文字体)
    # -----------------------------------------------------------
    system_name = platform.system()
    if system_name == "Windows":
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
    elif system_name == "Darwin":  # macOS
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC']
    else:  # Linux/Server
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'SimHei']
    
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # -----------------------------------------------------------
    # 2. 数据读取与预处理 (增强版：自动处理编码错误与表头清洗)
    # -----------------------------------------------------------
    df = None
    # 定义尝试的编码列表
    # 修改：将 gb18030/gbk 放在最前面，因为很多中文 CSV 默认是 GBK，
    # 且 utf-8 有时会错误地解码 GBK 而不报错（导致乱码）。
    encodings_to_try = ['utf-8','gb18030', 'gbk', 'utf-8-sig', 'utf-8', 'utf-16']
    
    for encoding in encodings_to_try:
        try:
            # 尝试读取，使用 engine='python' 容错率更高
            # 跳过前两行元数据
            temp_df = pd.read_csv(file_path, skiprows=2, encoding=encoding, engine='python')
            
            # --- 乱码检测逻辑 ---
            # 有时候 utf-8 可以读取 gbk 文件不报错，但内容是乱码（如 'ָ'）。
            # 我们检查列名中是否包含预期的中文字符（'指标' 或 '年'）。
            # 如果列名里完全没有这两个字，很有可能是乱码，我们强制抛出异常以尝试下一个编码。
            cols_str = "".join([str(c) for c in temp_df.columns])
            if '指标' not in cols_str and '年' not in cols_str:
                 # 这是一个假成功，实际上是乱码
                 continue
            
            df = temp_df
            print(f"成功使用 {encoding} 编码读取文件")
            break
        except Exception as e:
            # 如果当前编码失败，尝试下一个
            continue

    if df is None:
        print(f"错误：无法读取文件 {file_path}。请检查文件是否存在或是否损坏。")
        return

    # --- 关键修复：清洗列名 ---
    # 去除列名两端的空格
    df.columns = df.columns.str.strip()
    
    # 检查 '指标' 列是否存在
    if '指标' not in df.columns:
        # 尝试查找包含 '指标' 的列名（处理特殊字符残留或OCR错误）
        potential_cols = [c for c in df.columns if '指标' in str(c)]
        if potential_cols:
            print(f"警告：未找到精确的'指标'列，但找到 '{potential_cols[0]}'，将自动重命名。")
            df.rename(columns={potential_cols[0]: '指标'}, inplace=True)
        else:
            print("错误：数据中未找到'指标'列。")
            print(f"实际读取到的列名如下，请检查 skiprows 设置是否正确: \n{df.columns.tolist()}")
            return

    # 定义需要的指标
    indicators = {
        'import': '高技术产品进口额(亿美元)',
        'export': '高技术产品出口额(亿美元)',
        'market': '技术市场成交额(亿元)'
    }

    mask = df['指标'].isin(indicators.values())
    df_subset = df[mask].copy()
    
    if df_subset.empty:
        print("错误：未找到指定指标的数据。请检查CSV文件中的指标名称是否与代码中一致。")
        return

    # 转置数据：将年份作为索引 (行)，指标作为列
    df_plot = df_subset.set_index('指标').T
    df_plot.index.name = 'Year'

    # 清洗索引：去除“年”字并转换为整数，以便排序
    # 注意：原始数据列名如 '2024年', '2023年'...
    # 使用 regex=False 避免警告
    df_plot.index = df_plot.index.astype(str).str.replace('年', '', regex=False)
    # 过滤掉非数字的行（如备注等）
    df_plot = df_plot[df_plot.index.str.isnumeric()]
    df_plot.index = df_plot.index.astype(int)
    
    # 按年份升序排列 (2015 -> 2024)
    df_plot = df_plot.sort_index()

    # 将数据列转换为数值类型 (处理可能的 NaN)
    for col in df_plot.columns:
        df_plot[col] = pd.to_numeric(df_plot[col], errors='coerce')

    # 提取绘图所需的具体序列，方便调用
    years = df_plot.index
    # 使用 .get() 方法防止列名不匹配报错
    s_import = df_plot.get(indicators['import'])
    s_export = df_plot.get(indicators['export'])
    s_market = df_plot.get(indicators['market'])

    # -----------------------------------------------------------
    # 3. 绘图逻辑
    # -----------------------------------------------------------
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # --- 左轴 (Ax1)：高技术产品进出口 (堆叠柱状图) ---
    bar_width = 0.5
    
    # 绘制进口 (底部柱子)
    p1 = ax1.bar(years, s_import, width=bar_width, 
                 label='高技术产品进口额', color='#729ece', alpha=0.85, zorder=10)
    
    # 绘制出口 (顶部柱子，bottom参数设为进口额)
    p2 = ax1.bar(years, s_export, width=bar_width, bottom=s_import, 
                 label='高技术产品出口额', color='#ff9e4a', alpha=0.85, zorder=10)

    # 设置左轴标签和样式
    ax1.set_xlabel('年份', fontsize=12, labelpad=10)
    ax1.set_ylabel('高技术产品进出口额 (亿美元)', fontsize=12, color='#333333', fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#333333')
    ax1.set_title('2015-2024年 高技术产品贸易与技术市场成交额趋势对比', fontsize=16, pad=20)
    
    # 设置X轴刻度为所有年份 (确保显示完整)
    ax1.set_xticks(years)
    ax1.grid(True, axis='y', linestyle='--', alpha=0.3, zorder=0)

    # --- 右轴 (Ax2)：技术市场成交额 (折线图) ---
    ax2 = ax1.twinx()
    
    p3 = ax2.plot(years, s_market, color='#d62728', linewidth=2.5, marker='o', 
                  markersize=8, label='技术市场成交额', zorder=20)

    # 设置右轴标签和样式
    ax2.set_ylabel('技术市场成交额 (亿元)', fontsize=12, color='#d62728', fontweight='bold', labelpad=10)
    ax2.tick_params(axis='y', labelcolor='#d62728')

    # --- 图例合并 ---
    # 获取两个轴的图例句柄和标签
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    
    # 合并显示在左上角
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left', 
               frameon=True, shadow=True, fancybox=True, fontsize=10)

    # --- 添加数据标注 (可选，增强可读性) ---
    # 为最新的有效数据添加数值标签
    last_valid_idx = s_market.last_valid_index()
    if last_valid_idx:
        last_val = s_market.loc[last_valid_idx]
        ax2.annotate(f'{last_val:.0f}', 
                     xy=(last_valid_idx, last_val), 
                     xytext=(0, 10), textcoords='offset points', 
                     ha='center', color='#d62728', fontweight='bold')

    plt.tight_layout()
    
    # 保存图片
    output_filename = 'tech_trade_analysis.png'
    plt.savefig(output_filename, dpi=300)
    print(f"图表已成功保存为: {output_filename}")
    
    # 显示图表
    plt.show()

if __name__ == "__main__":
    # 请确保csv文件在当前目录下，或者修改此路径
    csv_file = 'data.csv'
    plot_tech_stats(csv_file)