age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $4.")
else:
    print("Your admission cost is $8.")

age=13
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("Your admission cost is $"+str(price))