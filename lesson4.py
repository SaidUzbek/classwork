age = int(input('Сколько тебе лет?'))
if(age>=18):
    print('Добро пожаловать!')
else:
    print('Пошёл отсюда малолетка!')

    






year = int(input('Введите код'))
if year%400==0:
    print('Високосный год')
elif year%4==0:
    if year %100!=0:
        print('Високосный год')
else:
    print('Не високосный год')
else:
    print('Не високосный год')