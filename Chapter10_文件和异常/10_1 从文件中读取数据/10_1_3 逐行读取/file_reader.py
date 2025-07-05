filename='pi_digit.txt'
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())