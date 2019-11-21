# Запрашиваем число и сразу переводим в формат integer
value = int(input('Введите число '))

# Прибавляем к этому числу 2 и выводим
print('Твое число + 2 будет ', value + 2)

# Запрашиваем число пока оно не станет больше 0, но меньше 10

while True:
    value_2 = int(input('Введите число '))
    if value_2 >0 and value_2 < 10 :
        print ('Молодец, твое число в квадрате будет ', value_2 ** 2)
        break
    elif value_2 <= 0:
        print('Не, слишком мало, давай еще раз, от 0 до 10 попробуй')
    else:
        print('Не, это слишком много, от 0 до 10 попробуй')

# А теперь программа Медицинская карта

print ('Ну теперь давай познакомимся', ' я тебе дам советы про здоровье))',sep=',')

name = str(input('Ваше Имя : '))
surname = str(input('Ваша Фамилия : '))
age = int(input('Возраст : '))
weight = int(input('А сколько ты весишь? '))

if (age <= 30 and (weight > 120 or weight < 50)) or ((age > 30 and age <= 40) and (weight < 50 or weight > 120)):
    print(name, surname, 'возраст ', age, 'вес ', weight, ' - следует заняться собой!')
elif age >= 40 and (weight < 50 or weight > 120):
    print(name, surname, 'возраст ', age, 'вес ', weight, ' - следует обратиться к врачу!')
else:
    print(name, surname, 'возраст ', age, 'вес ', weight, ' - в хорошем состоянии!')

