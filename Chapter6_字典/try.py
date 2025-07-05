#6-1 人：
people={"first_name":"huang","last_name":"xiangdong","city":"qingdao"}
print(people)

#6-2 喜欢的数字
favorite_numbers={
    'huang':1,
    'han':2,
    'lin':3,
    'guo':4
}
print(favorite_numbers['huang'])
print(favorite_numbers['han'])
print(favorite_numbers['lin'])
print(favorite_numbers['guo'])

#6-3 词汇表:
glossary={
    'list':'a collection of items in a particular order',
    'for':'used to iterate over a sequence',
    'if':'used to make decisions in your code',
    'dictionary':'a collection of key-value pairs',
    'tuple':'an immutable list'
}
print("list: "+glossary['list'] )

#6-4 词汇表2：
for word,meaning in glossary.items():
    print(word+": "+meaning)

#6-5 河流
rivers={
    'yangtze':'china',
    'yellow river':'china',
    'nile':'egypt'
}
for river, country in rivers.items():
    print("The "+river+" runs through "+country+".")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

#6-6 调查
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
needpolls=['jen','huang','sarah','lin']
for name in needpolls:
    if name in favorite_languages.keys():
        print(name+": Thank you for taking the poll.")
    else:
        print(name+": Sorry, please taking the poll.")

#6-7 人、
people=[{
        'first_name':'huang',
        'last_name':'xiangdong',
        'location':'qingdao',
    },
    {
        'first_name':'han',
        'last_name':'chengzhi',
        'location':'xian',
    },
    {
        'first_name':'lin',
        'last_name':'yong',
        'location':'beijing',
    }]
for user in people:
    print(user)
    full_name=user['first_name']+" "+user['last_name']
    location=user['location']

#6-8 宠物：
pet1={'han':'dog','host':'huang'}
pet2={'lin':'cat','host':'xiang'}
pets=[pet1,pet2]
for pet in pets:
    print(pet)

#6-9 喜欢的地方：
favorite_places={
    'huang':['qingdao','haikou','singapore'],
    'han':['xian','tokyo'],
    'lin':['guangzhou','shenzhen'],
}
for name,favorite_place in favorite_places.items():
    print("\n"+name.title()+"'s favorite places are:")
    for place in favorite_place:
        print(place.title())

#6-10 喜欢的数字:
favorite_numbers={
    'huang':[1,2,3,4],
    'han':[5,6,7,8],
    'lin':[9,10,11,12],
}
for name,numbers in favorite_numbers.items():
    print("\n"+name.title()+"'s favorite numbers are:")
    for number in numbers:
        print(number)

#6-11 城市：
cities={
    'qingdao':{'country':'China','population':10000000,'fact':'beautiful'},
    'xian':{'country':'China','population':5000000,'fact':'ancient'},
    'shanghai':{'country':'China','population':20000000,'fact':'modern'},
}
for city,city_info in cities.items():
    print("\nCity: "+city)
    print("\tCountry: "+city_info['country'])
    print("\tPopulation: "+str(city_info['population']))
    print("\tFact: "+city_info['fact'])