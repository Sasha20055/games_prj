import random
from time import sleep


def is_valid(a):
    return 0 < int(a) <= border


def new_game(num):
    if num == 'д':
        return game(), True
    else:
        timer()
        print('Спасибо что поиграли в нашу игру;)')
        return False

def timer():
    sleep(0.3)
    print('.')
    sleep(0.3)


def game():
    print("Приветствую в игру 'Числовая Угадайка'")
    timer()
    global border
    border = int(input('Введите правую границу загаданного числа: '))
    print('Угадайте загаданное число')
    b = randint(1, border)  # случайное число
    counter = 0
    while True:
        a = int(input())
        timer()
        if is_valid(a) == False:
            print(f'Число должно быть от 1 до {border}')
        elif a > b:
            print('Слишком много, попробуйте еще раз')
            counter += 1
        elif a < b:
            print('Слишком мало, попробуйте еще раз')
            counter += 1
        else:
            print('Вы угадали, поздравляем!')
            counter += 1
            if counter == 0:
                print('Угадали с первой попытки!')
            else:
                print(f'Ваше количество попыток:{counter}')
            break


n = True
try:
    game()
except ValueError:
    print('Вводить только цифры!')
while n:
    print('Хотите сыграть ещё раз? (д/н)')
    n = new_game(input())
