def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename,encoding='UTF-8') as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #计算文件大致包含多少个单词
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)