from pathlib import Path
import csv

path=Path('weather_data/sitka_weather_07-2021_simple.csv')
lines=path.read_text().splitlines()
"""path.read_text() 读取整个文件内容，返回一个字符串。
splitlines() 将这个字符串按行拆分，返回一个行的列表。"""

reader=csv.reader(lines) #创建一个reader对象
header_row=next(reader) #返回下一行，第一次返回首行

#提取最高温度
highs=[]
for row in reader:
    high=int(row[4])
    highs.append(high)
print(highs)