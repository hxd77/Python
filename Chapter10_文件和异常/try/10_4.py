#访客名单
filename='guess_book.txt'
with (open(filename,'a') as file_object):
    while True:
        name=input("Please enter your name and enter 'q' to quit: ")
        if name=='q':
            break
        else:
            name='Hello '+name+'\n'
            print(name)
            file_object.write(name)
