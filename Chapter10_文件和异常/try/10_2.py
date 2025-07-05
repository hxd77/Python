with open('learning_python.txt') as file_object:
    for line in file_object:
        line=line.replace('Python','C')
        print(line.rstrip())