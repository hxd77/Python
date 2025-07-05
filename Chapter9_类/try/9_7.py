# 管理员
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

class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        '''显示管理员权限'''
        print("Admin privileges are:")
        for privilege in self.privileges:
            print("- "+privilege)

admin=Admin('zhang','san',18,'beijing')
admin.greet_user()
admin.show_privileges()
