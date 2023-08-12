from Cat import Cat_pet_house

cat1=Cat_pet_house("Барон","Мальчик","2 года")
cat2=Cat_pet_house("Сэм","Мальчик","2 года")

#первый вариант
print("cat1.name=", cat1.name)
print("cat1.gender=", cat1.gender)
print("cat1.age=", cat1.age)


print("cat2.name=", cat2.name)
print("cat2.gender=", cat2.gender)
print("cat2.age=", cat2.age)


#второй вариант
print(f"""Имя: {cat1.getName()}
Пол: {cat1.getGender()}
Возраст: {cat1.getAge()}
----------------""")
print(f"""Имя: {cat2.getName()}
Пол: {cat2.getGender()}
Возраст: {cat2.getAge()}
----------------""")
