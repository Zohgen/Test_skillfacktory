count_ticket=int(input("Введите количество билетов: \n"))
while count_ticket<1:
    print("Некорректное кол-во билетов!\n")
    count_ticket = int(input("Введите количество билетов: \n"))
a=0
b=0
c=0
summa=0
for i in range (count_ticket):
    age = int(input("Введите возраст: \n"))
    while age < 1:
        print("Некорректный возраст!\n")
        age = int(input("Введите возраст: \n"))
    if(age<18):
        #print("Этот билетик бесплатный :) \n")
        a=0
    elif(18<=age<=25):
        #print("Билетик стоит : 990 рублей \n")
        b+=990
    elif(age>25):
        #print("Билетик стоит : 1390 рублей \n")
        c+=1390
summa=b+c
if(count_ticket>3):
    summa*=0.9
    print("У вас больше 3х билетов, скидка 10%, к оплате :",summa, "рублей \n")
elif(1<=count_ticket<=2):
    print("К оплате :",summa," рублей \n")
