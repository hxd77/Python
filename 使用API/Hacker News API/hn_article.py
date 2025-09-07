import requests
import json

#执行API调用并存储响应
url='https://hacker-news.firebaseio.com/v0/item/31353677.json'
r=requests.get(url)
print(f"Status code: {r.status_code}")

#探索数据的结构
response_dict=r.json() #json()方法将JSON格式的响应内容转换为Python字典
response_string=json.dumps(response_dict,indent=4)#将Python对象转换为JSON字符串，indent参数指定4个空格缩进
print(response_string)