from pathlib import Path
import json

#将数据作为字符串读取并转换未Python对象
path=Path('eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)
"""json.loads()：json.loads() 是 Python json 模块中的一个方法，用于将 JSON 格式的字符串 转换为 Python 数据类型（如字典、列表等）。"""

#将数据文件转换为更易于阅读的版本
path=Path('eq_data/readable_eq_data.geojson')
readable_contents=json.dumps(all_eq_data,indent=4)
"""json.dumps()：json.dumps() 是 Python json 模块中的一个方法，用于将 Python 数据类型（如字典、列表、元组等）转换成 JSON 格式的字符串。dumps 是 "dump string" 的缩写，即将数据转化为 JSON 格式的字符串。

all_eq_data：这是你要转换为 JSON 格式的 Python 数据，可以是一个字典、列表、元组、字符串等。这里假设 all_eq_data 是一个 Python 对象，可能是包含多个数据的字典或列表。

indent=4：这个参数指定了 格式化输出时每一级嵌套的缩进空格数。

如果没有设置 indent，生成的 JSON 字符串将是 紧凑的，没有换行和缩进。

设置 indent=4 后，JSON 字符串将被 格式化，每一级嵌套将缩进 4 个空格，使得结果更加易读。"""
path.write_text(readable_contents)