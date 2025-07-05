#喜欢的数字
import json

favorite_number=input("Please enter your favorite number:")
filename='favorite_number.json'
with open(filename,'w') as f_obj:
    json.dump(favorite_number,f_obj)

with open(filename) as f_obj:
    number=json.load(f_obj)

print("I know your favorite number, " + number + "!")
