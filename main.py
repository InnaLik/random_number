import random
print('Угадайте число')
k = int(input('Введите число: '))
num = random.randrange(101)
while k != num:
    if k > num:
        print('Слишком большое число')
    if k < num:
        print('Слишком маленькое число')
    k = int(input('Введите число: '))
if k == num:
    print('Поздравляю, вы угадали!')