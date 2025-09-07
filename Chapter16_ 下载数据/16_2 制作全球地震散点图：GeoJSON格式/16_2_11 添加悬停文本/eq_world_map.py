import plotly.express as px
from pathlib import Path
import pandas as pd
import json

#将数据作为字符串读取并转换未Python对象
path=Path('eq_data/eq_data_30_day_m1.geojson')
try:
    contents=path.read_text()
except:
    contents=path.read_text(encoding='utf-8')
all_eq_data=json.loads(contents)
"""json.loads()：json.loads() 是 Python json 模块中的一个方法，用于将 JSON 格式的字符串 转换为 Python 数据类型（如字典、列表等）。"""
#查看数据集中的所有地震
all_eq_dicts=all_eq_data['features']

mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]#geometry健关联的字典中有一个coordinates键，关联一个列表，前两个值为经度和纬度
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data=pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','维度','位置','震级']
)
'''zip函数按行打包，得到一个表格
| 经度    | 维度   | 位置  | 震级  |
| ----- | ---- | --- | --- |
| 100.1 | 30.5 | 地震A | 5.1 |
| 101.2 | 31.6 | 地震B | 6.2 |
'''


data.head()#返回前五行数据

fig=px.scatter(
    data,
    x='经度',
    y='维度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10, #尺寸缩小为10像素
    color='震级',#从蓝到红到黄
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()
