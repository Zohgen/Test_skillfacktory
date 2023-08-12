class Cat_pet_house:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getGAge(self):
        return self.age

    #def init_from_dict(self, event_dict):
     #   self.name = event_dict.get("name")
      #  self.gender = event_dict.get("gender")
       # self.age = event_dict.get("age")


# cats=[
#     {
#         "name" : "Барон",
#         "gender" : "Мальчик",
#         "age" : "2 года",
#     },
#     {
#         "name": "Сэм",
#         "gender": "Мальчик",
#         "age": "2 years",
#     },
# ]
# for event in cats:
#     event_obj = Cat_pet_house()
#     event_obj.init_from_dict(event)
#     print(event_obj.name,event_obj.gender,event_obj.age)