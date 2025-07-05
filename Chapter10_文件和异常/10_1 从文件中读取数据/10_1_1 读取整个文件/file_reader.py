with open('pi_digits.txt', 'r') as file_object:
    contents=file_object.read()
    print(contents)
    print(contents.rstrip())
