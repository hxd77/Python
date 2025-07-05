#8-1 消息
def display_message():
    print("Your are learning is function")
display_message()

#8-2 喜欢的图书
def favorite_book(title):
    print("One of my favorite books is "+title)

favorite_book("Alice in Wonderland")

#8-3 T恤
def make_shirt(size,font):
    print("This is a shirt with "+size+" size and "+font+" font ")
make_shirt('medium','hhh')

#8-4 大号T恤
def make_shirt(size='Large',font='I love Pyhon'):
    print("This is a shirt with " + size + " size and " + font + " font ")
make_shirt()
make_shirt('medium','hxd da shuaibi')

#8-5 城市
def descibe_city(cityname,country):
    print(cityname.title()+" is in "+country.title())
descibe_city('qingdao','China')

#8-6 城市名
def city_country(cityname,country):
    string=cityname+", "+country
    return string.title()
print(city_country('Santiago','Chile'))

#8-7 专辑
def make_album(singer_name,album_name,song_num=''):
    message={'singer':singer_name,'album':album_name}
    if song_num:
        message['song'] = song_num
    return message
message=make_album("zhoujielun",'qinghuaci',11)
print(message)

#8-8 用户的专辑
while True:
    print("\nPlease enter singername")
    print("enter 'q' to quit")
    singername=input("Singername: ")
    if singername=='q':
        break
    albumname = input("Albumname: ")
    if albumname=='q':
        break
    message=make_album(singername,albumname)
    print(message)

#8-9 魔术师
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
magicians=['huang','han','xiang','lin']
show_magicians(magicians)

#8-10 了不起的魔术师
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'Great '+magicians[i]
    return magicians

magicians = make_great(magicians)
print(magicians)

#8-11 不变的魔术师
magicians=['huang','han','xiang','dong','lin']
magicians1=make_great(magicians[:])
print(magicians)
print(magicians1)

#8-12 三明治
def collet_sandwich(*toppings):
    for topping in toppings:
        print("Adding "+topping+" to the sandwich")




