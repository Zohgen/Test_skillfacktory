from api import PetFriends
from settings import valid_email, valid_password
import os
pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email,password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""
    status,result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """

    _,auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets'])>0

def test_add_new_pet_with_valid_key(name='Мурзик', animal_type='кот',age='3',pet_photo='images/kotik.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo=os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == 'кот'

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key,"Сова", "птица", "5", "images/Filin.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='ДедБомБом', animal_type='кот', age='3'):
    """Проверяем возможность обновления информации о питомце"""
    #обновление инфы пета
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_successful_update_self_pet_photo(pet_photo = 'images/Filin.jpg'):
    """Проверяем возможность добавления фото для питомца"""
    #добавление фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
        assert result['pet_photo'] != pet_photo

    else:
        raise Exception("There is no my pets")


def test_create_pet_simple(name='Мурзик', animal_type='кот', age='3'):
    """Проверяем что можно добавить питомца без фото с корректными данными"""
    #создание пета без фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

#1
def test_change_name(name='@!@&#(!@', animal_type='', age=''):
    """Проверяем возможность сменить имя питомомца на символы"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

#2
def test_change_age(name='', animal_type='', age='-1'):
    """Проверяем возможность сменить возраст питомомца на отрицательный"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['age'] == age
    else:
        raise Exception("There is no my pets")

#3
def test_change_anymal_type(name='', animal_type='      ', age=''):
    """Проверяем возможность сменить тип питомомца на пустое поле(пробелы)"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['animal_type'] == animal_type
    else:
        raise Exception("There is no my pets")

#4
def test_add_animal_without_age(name='Чупик', animal_type='Мурлозавр', age=''):
    """Проверяем что можно добавить питомца без возраста с корректными данными"""
    #добавление нового пета без возраста
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['age'] == age


#5
def test_add_animal_without_name(name='', animal_type='Мурлозавр', age='1087'):
    """Проверяем что можно добавить питомца без имени с корректными данными"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

#6
def test_change_name_number(name='123', animal_type='Мурлозавр', age='1087'):
    """Проверяем возможность сменить имя питомомца на число"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == age
    else:
        raise Exception("There is no my pets")

#7
def test_change_animal_type_number(name='', animal_type='32094', age=''):
    """Проверяем возможность сменить тип питомомца на число"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200

        assert result['animal_type'] == animal_type

    else:
        raise Exception("There is no my pets")


#8
def test_successful_delete_self_pet_without_photo():
    """Проверяем возможность удалить питомомца без фото"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet_without_photo(auth_key,"Сова", "птица", "5")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


#9
def test_check_valid_password(email=valid_email,password="asd213"):
    """Проверяем возможность ввода неверного password"""
    status,result = pf.get_api_key(email, password)
    assert status == 403
    if (status == 403):
        raise Exception('not valid password or email')

#10
def test_check_valid_email(email='213@#$%!  ',password=valid_password):
    """Проверяем возможность ввода неверного email"""
    status,result = pf.get_api_key(email, password)
    assert status == 403
    if (status == 403):
        raise Exception('not valid password or email')

