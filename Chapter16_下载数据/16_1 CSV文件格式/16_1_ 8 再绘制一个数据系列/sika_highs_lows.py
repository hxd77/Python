from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path=Path('weather_data/sitka_weather_2021_simple.csv')
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header=next(reader)

#提取日期、最高温度和最低温度
dates,highs,lows=[],[],[]
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    high=int(row[4])
    low=int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

#根据数据绘图
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots() #fig是图形，ax是坐标轴
ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=14)
plt.show()
