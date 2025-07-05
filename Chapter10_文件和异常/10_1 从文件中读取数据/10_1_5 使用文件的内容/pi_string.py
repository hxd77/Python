from pyasn1.type.char import PrintableString

filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
print(lines)
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))