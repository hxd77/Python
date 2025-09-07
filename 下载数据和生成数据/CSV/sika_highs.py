from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path=Path('weather_data/sitka_weather_2021_simple.csv')
lines=path.read_text().splitlines()
"""path.read_text() 读取整个文件内容，返回一个字符串。
splitlines() 将这个字符串按行拆分，返回一个行的列表。每一行是一个值"""

reader=csv.reader(lines) #创建一个reader对象
header_row=next(reader) #返回下一行，第一次返回首行

#提取日期和最高温度
dates,highs=[],[]
for row in reader:
    current_date=datetime.strptime(row[2], '%Y-%m-%d') #将指定格式的字符串转换为datetime对象
    high=int(row[4])
    dates.append(current_date)
    highs.append(high)

#根据最高温度绘图
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates,highs,color='red')

#设置绘图的格式
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() #倾斜的日期标签
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
