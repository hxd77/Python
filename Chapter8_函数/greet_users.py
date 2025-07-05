def greet_users(names):
    '''向列表中的每位用户发出简单的问候'''
    for name in names:
        msg='Hello, '+name.title()+"!"
        print(msg)
username=['hannah','ty','margot']
greet_users(username)