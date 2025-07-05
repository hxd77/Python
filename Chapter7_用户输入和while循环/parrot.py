propmt="\nTell me something, and I will repeat it back to you: "
propmt+="\nEnter 'quit' to end the program. "
active=True
#while message!='quit':
    #message=input(propmt)
    #if message!='quit':
        #print(message)
while active:
    message=input(propmt)

    if message=='quit':
        active=False
    else:
        print(message)