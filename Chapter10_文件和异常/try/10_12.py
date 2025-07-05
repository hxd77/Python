#记住喜欢的数字
import json

filename = 'favorite number.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
    print("I know your favorite number! It's " + number + ".")
except FileNotFoundError:
    favorite_num = input("Enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num, f_obj)