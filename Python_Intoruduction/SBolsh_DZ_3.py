# Логика игры очень простая - каждый раз делим возможный интервал ответов посередине

print('Игра угадай число')

print('Я буду выводить число, если оно больше загаданного тобой - нажими "<" если оно меньше - нажми ">"')
print ('Если я угадаю - тогда нажми "="')

answers = []
i = 1

# Cоздаем список ответов
while i < 101:
    answers.append(i)
    i +=1

# Это для отладки использовал
# print(answers)

reply = None
#import random
#pos = random.randint(1,100)
# Чтобы сдедать игру интереснее, я попрорбовал начинать со случайного числа, но мои наблюдения показали,
# что, в среднем, это приводит только к увеличению числа попыток
pos = 50

while reply != '=':
    guess = answers[pos]
    reply = input('Ты загадал число {} ?'.format(guess))
    if reply == '<':
        answers = answers[:pos]
#        print(answers)
    else:
        answers = answers[pos:]
#        print(answers)
    pos = int(len(answers)//2)

print(f'Ура, я угадал! Твое число {guess} !')