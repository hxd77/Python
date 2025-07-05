from pathlib import Path
import json

def get_stored_username(path):
    '''如果存储了用户名，则获取他'''
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)#json.loads()是从字符串中读取对象
        return username
    else:
        return None

def get_new_username(path):
    '''提示输入用户名'''
    username=input('What is your name? ')
    contents=json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    '''问候用户，并指出他是^新用户还是老用户'''
    path=Path('username.json')
    username=get_stored_username(path)
    if username:
        correct=input(f"Are you {username}? (y/n) ")
        if correct=='y':
            print('Welcome back, ' + username + '!')
    else:
        username=get_new_username(path)
        print(f'We\'ll remember you when you come back, {username}!')

greet_user()