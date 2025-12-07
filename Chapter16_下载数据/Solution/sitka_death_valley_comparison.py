from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_data(path,dates,highs,lows,date_index,high_index,low_index):
    """从一个数据文件中得到最高和最低温度"""
    lines=path.read_text().splitlines()
    reader=csv.reader(lines)
    header_row=next(reader)

    #提取日期和最高最低温度
    for row in reader:
        current_date=datetime.strptime(row[date_index],'%Y-%m-%d')
        try:
            high=int(row[high_index])
            low=int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#获取sitka的天气数据
path=Path('weather_data/sitka_weather_2021_simple.csv')
dates,highs,lows=[],[],[]
get_weather_data(path,dates,highs,lows,2,4,5)

#绘制sitka的图像
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.15)

#获取死亡谷的天气数据
path=Path('weather_data/death_valley_2021_simple.csv')
dates,highs,lows=[],[],[]
get_weather_data(path,dates,highs,lows,2,3,4)

#添加死亡谷的的天气数据到现在的图像上
ax.plot(dates,highs,color='red',alpha=0.3)
ax.plot(dates,lows,color='blue',alpha=0.3)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.05)

#图片格式
title="Daily High and Low Temperatures - 2021"
title+="\nSitka, AK and Death Valley, CA"
ax.set_title(title)
ax.set_xlabel("", fontsize=24)
ax.set_ylabel("Temperatures (F) ", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)
ax.set_ylim(10,140)
"""set_ylim(ymin, ymax) 是一个设置 y轴显示范围 的方法。它接受两个参数：

ymin：y轴的最小值（这里是 10）。

ymax：y轴的最大值（这里是 140）"""

plt.show()