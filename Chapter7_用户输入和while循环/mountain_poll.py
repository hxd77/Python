responses={}

#设置一个标志，指出调查是否继续
polling_active=True

while polling_active:
    #提示输入被调查者的名字和回答
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")

    #将答案存储在字典中
    responses[name]=response

    #看看是否还有人要参与调查
    repeat=input("Would you like to another person respond?(yes/no)?")
    if repeat=='no':
        polling_active=False


#调查结果，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name+" would like to climb "+response+".")
