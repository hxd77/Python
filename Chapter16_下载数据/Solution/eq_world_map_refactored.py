from pathlib import Path
import json
import plotly.express as px

path=Path('eq_data/eq_data_30_day_m1.geojson')
contents=path.read_text(encoding='utf-8')
all_eq_data=json.loads(contents)

all_eq_dicts=all_eq_data['features']

mags,lons,lats,eq_titles=[],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

title='Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()
'''这段代码是使用 Plotly Express 创建一个 地理散点图（scatter_geo）。它将地震数据（包括经纬度、震级等信息）绘制在一个地图上。'''
'''color_continuous_scale 用来设置颜色的渐变方式。这里使用 'Viridis' 颜色方案，这是一个从紫色到黄色的渐变色，通常用于表示从低到高的数值。地震震级较小的点会呈现较暗的颜色，而震级较大的点会呈现较亮的颜色。'''
'''labels 用于给图表中的轴或颜色映射添加标签。在这个例子中，'color' 对应震级（Magnitude），所以这个设置将颜色条的标签设置为 Magnitude。即，颜色条旁边的标签将显示为 “Magnitude” 来表示震级。'''
'''projection 用于设置地图的投影方式。'natural earth' 是一种常见的地理投影方式，适合用于全球视图。这种投影将地球的表面呈现为一个球形，适合展示全球范围的数据。'''