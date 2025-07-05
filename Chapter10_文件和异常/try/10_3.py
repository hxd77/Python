#访客
name=input("Enter your name: ")
filename='guess.txt'
with open(filename,'a') as file_object:
    file_object.write(name+'\n')