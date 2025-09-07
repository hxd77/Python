from pathlib import Path
import json

#将数据作为字符串读取并转换未Python对象
path=Path('eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
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

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
