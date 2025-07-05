#加法计算器
#加法运算
print("Please enter two numbers to add.")
print("Enter 'q' to quit.")
while True:
    first_number=input("\nFirst number:")
    if first_number=='q':
        break
    second_number = input("\nSecond number:")
    if second_number=='q':
        break
    try:
        answer=int(first_number)+int(second_number)
    except ValueError:
        print("Please enter a number.")
    else:
        print(first_number + "+" + second_number + "=" + str(answer))

