#关于编程的调查
filename="The reason of like programming.txt"
with open(filename,'a') as file_object:
    while True:
        reason=input("Please enter the reason of like programming and enter 'q' to quit: ")
        if reason=='q':
            break
        else:
            reason='I like programming because '+reason+'\n'
            print(reason)
            file_object.write(reason)