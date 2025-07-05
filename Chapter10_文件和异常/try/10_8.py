#猫和狗
filenames=['cats.txt','dogs.txt']
def read_file(filename):
    '''读取文件内容'''
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
            print(filename+" include:\n"+contents)
    except FileNotFoundError:
        msg="Sorry,the file " + filename + " does not exist."
        print(msg)
for filename in filenames:
    read_file(filename)