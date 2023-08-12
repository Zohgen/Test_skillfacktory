from Cat import Cat_pet_house


cats=[
    {
        "name" : "Барон",
        "gender" : "Мальчик",
        "age" : "2 года",
    },
    {
        "name": "Сэм",
        "gender": "man",
        "age": "2 years",
    },
]

cat=Cat_pet_house(cats)

# print("cat.name=",cat.name)
# print("cat.gender=", cat.gender)
# print("cat.age=", cat.age)
# for event in cats:
#     event_obj = Cat_pet_house()
#     event_obj.init_from_dict(event)
#     print(event_obj.name,event_obj.gender,event_obj.age)


print (cat)

