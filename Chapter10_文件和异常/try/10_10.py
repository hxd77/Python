#常见单词
filename="alice.txt"
try:
    with open(filename,encoding='UTF-8') as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry,the file "+filename+" does not exist."
    print(msg)
else:
    numbers=contents.lower().count('the')
    print("The file "+filename+" has "+str(numbers)+" times 'the'.")
