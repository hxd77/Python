from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path=Path('Chapter16_下载数据/Solution/weather_data/sitka_weather_2021_full.csv')
lines=path.read_text().splitlines()

reader = csv.reader(lines)
header_row= next(reader)

#提取日期和降雨量
dates,precips=[],[]
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    precip=float(row[5])
    dates.append(current_date)
    precips.append(precip)

#绘图
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.bar(dates,precips,color='blue')

#格式设置
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (inches)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()