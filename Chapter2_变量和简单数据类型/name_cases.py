#2-3 个性化消息:
from traceback import print_tb

user_name="Hello huang xingdong,would you like to learn some Python today?"
print(user_name)

#2-4 调整名字的大小写:
name="huang xiangdong"
print(name.upper())
print(name.lower())
print(name.title())

#2-5 名言:
print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\" ")

#2-6 名言2：
famous_person="Albert Einstein"
message="A person who never made a mistake never tried anything new."
print(famous_person+" once said, \""+message+"\"")

#2-7 剔除人名中的空白:
name=("  \thuang xiangdong  ")
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())