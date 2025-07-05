filename="alice.txt"
try:
    with open(filename,encoding='UTF-8') as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry,the file "+filename+" does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has "+str(num_words)+" words.")