import requests
import plotly.express as px

#执行API调用并查看响应
url='https://api.github.com/search/repositories'
url+='?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)#发送http的get请求headers 是一个字典，包含 HTTP 请求的头部信息。头部信息通常用于指定请求的类型、格式、身份验证等
print(f"Status code: {r.status_code}")

#处理结果
response=r.json()
print(f"Complete results: {not response['incomplete_results']}")

#处理有关仓库的信息
repo_dicts=response['items']
repo_name,stars,hover_texts=[],[],[]
for repo_dict in repo_dicts:
    repo_name.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    #创建悬停文本
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#可视化
title="Most-Starred Python Projects on GitHub"
labels={"x":"Repository","y":"Stars"}#添加x和y轴标题
fig=px.bar(x=repo_name,y=stars,title=title,labels=labels,hover_name=hover_texts)
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
#图形标题字号为28，坐标轴字号为20
fig.show()