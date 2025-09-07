import requests

#执行API调用并查看响应
url='https://api.github.com/search/repositories'
url+='?q=language:python+sort:stars+stars:>10000'
#API查询Github中star数超过10000的Python项目

headers={"Accept":"application/vnd.github.v3+json"}
'''Accept：这是一个 HTTP 请求头字段，表示客户端希望从服务器接收的数据格式。客户端通过这个字段告诉服务器，它能接受什么格式的数据响应。
application/vnd.github.v3+json：这是 GitHub API 的一种媒体类型（MIME 类型），告诉 GitHub API 客户端希望接收的响应格式是 JSON 格式，且符合 GitHub API v3 版本的规范。
'''

r=requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")

#将响应转化为字典
response_dict=r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not (response_dict['incomplete_results'])}")

#探索有关仓库的信息
repo_dicts=response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#研究第一个仓库
repo_dict=repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}") #有多少项信息
for key in sorted(repo_dict.keys()): #sorted只是临时有顺序
    print(key)
print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}") #项目名字
print(f"Owner: {repo_dict['owner']['login']}") #项目所有者登录名
print(f"Stars: {repo_dict['stargazers_count']}") #项目star数
print(f"Repository: {repo_dict['html_url']}") #项目网址
print(f"Created: {repo_dict['created_at']}") #项目创建时间
print(f"Updated: {repo_dict['updated_at']}") #项目更新时间
print(f"Description: {repo_dict['description']}") #项目描述

