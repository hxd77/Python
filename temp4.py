import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import platform

# Data Loading with robust error handling
file_path = "data.csv"
df = None
encodings_to_try = ['gb18030', 'gbk', 'utf-8']

for encoding in encodings_to_try:
    try:
        # Try python engine which is more robust to "Expected 1 fields..." errors
        df = pd.read_csv(file_path, skiprows=2, encoding=encoding, engine='python')
        break
    except Exception as e:
        continue

if df is not None:
    # --- Plot 1: Funding Structure (100% Stacked Area) ---
    indicators_struct = {
        'gov': '研究与试验发展政府资金经费支出(亿元)',
        'corp': '研究与试验发展企业资金经费支出(亿元)',
    }
    
    # Pre-process
    df_struct = df[df['指标'].isin(indicators_struct.values())].set_index('指标').T
    df_struct.index = df_struct.index.astype(str).str.replace('年', '', regex=False)
    df_struct = df_struct[df_struct.index.str.isnumeric()]
    df_struct.index = df_struct.index.astype(int)
    df_struct = df_struct.sort_index()
    for col in df_struct.columns:
        df_struct[col] = pd.to_numeric(df_struct[col], errors='coerce')
    
    # Dropna
    df_struct = df_struct.dropna()
    
    # Calc percentages
    gov = df_struct[indicators_struct['gov']]
    corp = df_struct[indicators_struct['corp']]
    total = gov + corp
    gov_pct = (gov / total) * 100
    corp_pct = (corp / total) * 100
    
    # Plotting
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.stackplot(df_struct.index, gov_pct, corp_pct, labels=['Government Funding', 'Corporate Funding'], colors=['#4c72b0', '#dd8452'], alpha=0.85)
    ax1.set_title('Structure of R&D Funding: Gov vs Corp (2015-2023)', fontsize=14)
    ax1.set_ylabel('Percentage (%)')
    ax1.yaxis.set_major_formatter(ticker.PercentFormatter())
    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)
    ax1.margins(x=0)
    plt.tight_layout()
    plt.savefig('funding_structure_fixed.png')
    
    # --- Plot 2: Trade vs Market (Dual Axis) ---
    indicators_trade = {
        'import': '高技术产品进口额(亿美元)',
        'export': '高技术产品出口额(亿美元)',
        'market': '技术市场成交额(亿元)'
    }
    
    df_trade = df[df['指标'].isin(indicators_trade.values())].set_index('指标').T
    df_trade.index = df_trade.index.astype(str).str.replace('年', '', regex=False)
    df_trade = df_trade[df_trade.index.str.isnumeric()]
    df_trade.index = df_trade.index.astype(int)
    df_trade = df_trade.sort_index()
    for col in df_trade.columns:
        df_trade[col] = pd.to_numeric(df_trade[col], errors='coerce')

    # Plotting
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    
    # Bar (Trade)
    width = 0.5
    p1 = ax2.bar(df_trade.index, df_trade[indicators_trade['import']], width, label='High-tech Imports (USD)', color='#729ece', alpha=0.85)
    p2 = ax2.bar(df_trade.index, df_trade[indicators_trade['export']], width, bottom=df_trade[indicators_trade['import']], label='High-tech Exports (USD)', color='#ff9e4a', alpha=0.85)
    
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Trade Volume (100M USD)', color='#333')
    ax2.set_title('High-tech Trade vs Tech Market Turnover', fontsize=14)
    
    # Line (Market)
    ax3 = ax2.twinx()
    p3 = ax3.plot(df_trade.index, df_trade[indicators_trade['market']], color='#d62728', linewidth=2.5, marker='o', label='Tech Market Turnover (CNY)')
    ax3.set_ylabel('Turnover (100M CNY)', color='#d62728')
    ax3.tick_params(axis='y', labelcolor='#d62728')
    
    # Legend
    lines, labels = ax2.get_legend_handles_labels()
    lines2, labels2 = ax3.get_legend_handles_labels()
    ax3.legend(lines + lines2, labels + labels2, loc='upper left')
    
    plt.tight_layout()
    plt.savefig('trade_vs_market_fixed.png')
    
    print("Plots generated successfully.")
else:
    print("Failed to read dataframe.")