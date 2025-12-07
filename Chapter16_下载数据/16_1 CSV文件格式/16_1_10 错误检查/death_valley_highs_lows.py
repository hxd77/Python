from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path=Path('weather_data/death_valley_2021_simple.csv')
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header=next(reader)

#提取日期、最高温度和最低温度
dates,highs,lows=[],[],[]
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high=int(row[3])
        low=int(row[4])
    except:
        print(f"Missing data for {current_date}.")
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#根据数据绘图
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots() #fig是图形，ax是坐标轴
ax.plot(dates,highs,color='red',alpha=0.5) #alpha表示线条透明度
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
"""接受一组x值和两组y值，并用颜色填充两组y值之间的空间"""
ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=20)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=14)
plt.show()
