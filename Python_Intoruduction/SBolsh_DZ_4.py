# Задание 1. Напишите функцию, которая спрашивает имя, возраст и город проживания и возвращает потом эти данные

print('Задание № 1')

def input_func():
    name = input('Ваше имя : ')
    age = input('Ваш возраст : ')
    city = input('Ваш город : ')
    print('{}, {} год(а) проживает в городе {}'.format(name,age,city))

input_func()

# Задание 2. Напишите функцию, которая возвращает наибольшее число из трех

print('Задание № 2')

def max_func():
    list = []
    for number in range(3):
        number = int(input('Введите число : '))
        list.append(number)
    print('Наибольшее число :')
    print(max(list))

max_func()

# Задание 3. Создайте функцию "Атака"

print ('Задение № 3')

username = input('Введите имя игрока: ')
player = {
    'name' : username,
    'health' : 100,
    'damage' : 50}

enemy = {
    'name' : 'Злодей',
    'health' : 100,
    'damage' : 50}

print ('Идет сражение между')
print ('{} и {}'.format(player,enemy))

def attack (player1,player2):
    player1['health'] = player1['health'] - player2['damage']

print ('{} атакует {}'.format(enemy['name'],player['name']))

attack(player,enemy)

print (f'В результате: {player}')

#Задание 4. Усложните функцию "Атака" функцией "Броня"

player['armor'] = 1.2
enemy['armor'] = 1.2

def damage(player1,player2):
    result = player2['damage'] / player1['armor']
    return result

def new_attack(player1,player2,damage):
    player1['health'] = player1['health'] - damage(player1,player2)

print ('{} опять атакует {}, но {} в броне'.format(enemy['name'],player['name'],player['name']))

new_attack(player,enemy,damage)

print (f'В результате: {player}')
