from random import randint


target = randint(1, 10)
print(target)
guess = int(input('Введите вашу догадку: '))
while guess != target:
    if guess < target:
        print('Ваше предположение меньше загаданного числа')
    else:
        print('Ваше предположение больше загаданного числа')
    guess = int(input('Введите вашу догадку: '))
print('Вы угадали число!')
