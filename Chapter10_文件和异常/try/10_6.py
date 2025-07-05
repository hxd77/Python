#加法运算
print("Please enter two numbers to add.")

first_number=input("\nFirst number:")
second_number=input("\nSecond number:")

try:
    answer=int(first_number)+int(second_number)
    print(first_number+"+"+second_number+"="+str(answer))
except ValueError:
    print("Please enter a number.")

