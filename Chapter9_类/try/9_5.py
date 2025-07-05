#尝试登录次数
#用户
class User:
    def __init__(self,first_name,last_name,age,location):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
        self.username=first_name.title()+" "+last_name
        self.login_attempts=0
    def describe_user(self):
        print("User name is "+self.first_name.title()+" "+self.last_name)
        print("User age is "+str(self.age))
        print("User location is "+self.location.title())
    def greet_user(self):
        print("Welcome "+self.username+"!")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0
    def read_login_attempts(self):
        print("Login attempts is "+str(self.login_attempts))
user1=User("zhang","san",18,"beijing")
user2=User("li",'si',20,'shanghai')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

for i in range(10):
    user1.increment_login_attempts()

user1.read_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()