from pathlib import Path
import json

#将数据作为字符串读取并转换未Python对象
path=Path('eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)
"""json.loads()：json.loads() 是 Python json 模块中的一个方法，用于将 JSON 格式的字符串 转换为 Python 数据类型（如字典、列表等）。"""
#查看数据集中的所有地震
all_eq_dicts=all_eq_data['features']

mags=[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    mags.append(mag)
print(mags[:10])
