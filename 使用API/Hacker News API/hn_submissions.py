from operator import itemgetter

import requests

#执行API调用并查看响应
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f"Status code: {r.status_code}")

#处理有关每篇文章的信息
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:5]:
    #对于每篇文章，都执行一个API调用
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    requests_dict=r.json()

    #对于每篇文章，都创建一个字典
    submission_dict={
        'title':requests_dict['title'],
        'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
        'comments':requests_dict['descendants']#评论数
    }
    submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts, key=itemgetter('comments'), reverse=True)#reverse=True表示降序排列 使用operator模块中的函数itemgetter()，根据字典中的'comments'键对列表进行排序

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

