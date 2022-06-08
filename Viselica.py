# Виселица
from random import *
from time import sleep

ing_al = 'abcdefghigclmnopqrstuvwxyz'
word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
             "власть",
             "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин",
             "председатель",
             "сотрудник", "республика", "личность"]
word_car = ['Универсал', "минивен", "кроссовер", "купе", "кабриолет", "пикап", "седан", "шина", "диски"]
word_flo = ["роза", "альстромерия", "лилии", "тюльпаны", "хризантема", "архидея", "астры", "ландиши", "гербера"]
word_school = ["карандаш", "ручка", "пинал", "портфель", "доска", "учитель", "ученик", "парта"]


def display_hangman(tries):
    if tries == 8:
        print()
        for i in range(4):
            print('!', end='\n')
        print('-', )
    if tries == 7:
        print('-' * 8)
        for i in range(4):
            print('!', end='\n')
        print('-', )
    if tries == 6:
        print('-' * 8, '!      !', sep='\n', end='\n')
        for i in range(4):
            print('!', end='\n')
        print('-', )
    if tries == 5:
        print('-' * 8, '!      !', '!      0', sep='\n', end='\n')
        for i in range(3):
            print('!', end='\n')
        print('-', )
    if tries == 4:
        print('-' * 8, '!      !', '!      0', sep='\n', end='\n')
        print('!      !', '!      !', '!', sep='\n')
        print('-', )
    if tries == 3:
        print('-' * 8, '!      !', '!    * 0 ', sep='\n', end='\n')
        print('!     \!', '!      !', '!', sep='\n')
        print('-', )
    if tries == 2:
        print('-' * 8, '!      !', '!    * 0 *', sep='\n', end='\n')
        print('!     \!/', '!      !', '!     ', sep='\n')
        print('-', )
    if tries == 1:
        print('-' * 8, '!      !', '!    * 0 *', sep='\n', end='\n')
        print('!     \!/', '!      !', '!     / ', sep='\n')
        print('-', )
    if tries == 0:
        print('-' * 8, '!      !', '!    * 0 *', sep='\n', end='\n')
        print('!     \!/', '!      !', '!     / \\', sep='\n')
        print('-          DEAD')


def get_word():
    catalog = int(input('Выберите тематику слова\n(1)автомобиль (2)цветы (3)школа (4)любая\n==>  '))
    if catalog == 1:
        return choice(word_car)
    elif catalog == 2:
        return choice(word_flo)
    elif catalog == 3:
        return choice(word_school)
    elif catalog == 4:
        return choice(word_list)


def play(word):
    wed = int(input('Введите уровень сложности (1) , (2) , (3)\n==>  '))
    print('_' * 40)
    l_word = []
    l_word.extend(word)
    count = len(l_word)
    if wed == 1:
        trie = 9
        print(f'Первая буква слова {word[0]}, последняя {word[-1]}, всего в слове {len(word)} букв')
    elif wed == 2:
        trie = 7
        print(f'Первая буква слова {word[0]}, последняя {word[-1]}')
    else:
        trie = 7
    print('_' * 40)
    print(f'У вас {trie - 1} попыток')
    print('_' * 40)
    while True:
        sleep(0.5)
        gues = input('Введите предпологаемую букву в слове или само слово.\nВсе буквы маленькие\n==>  ').lower()
        if gues in ing_al:
            print('Игра РУССКОЯЗЫЧНАЯ...')
            sleep(0.5)
        if gues == word:
            print('Вы угадали!')
            break
        if gues in l_word:
            for i in range(len(l_word)):
                if l_word[i] == gues.lower():
                    print(f'Такая буква {i + 1} по списку')
                    count -= 1
                    print(f'Осталось {count} букв в слове')
                    sleep(0.5)
                    print('...')
                    sleep(0.5)
                    print('_' * 40)
        elif gues not in l_word:
            trie -= 1
            print(f'\nУ вас осталось {trie} попыток\n')
            print('_' * 17, end='\n')
            display_hangman(trie)
            print('_' * 17, end='\n')
            if trie == 0:
                print('Вы програли :(((')
                sleep(0.5)
                break
        if count == 0:
            finish_answ = input('Поздравляю, вы угадали все буквы, но что же это за слово?\n==>  ').lower()
            while True:
                if finish_answ == word:
                    print('Так точно!')
                    break
                else:
                    trie -= 1
                    print('_' * 17)
                    display_hangman(trie)
                    print('_' * 17)
                    print(f'Соберись, у тебя осталось {trie} попыток')
                    if trie == 0:
                        print('Вы програли :(((')
                        sleep(1)
                        print('_' * 17)
                        display_hangman(trie)
                        print('_' * 17)
                if trie == 0:
                    print('Очень жаль, вы проиграли   :(')
                    break
                finish_answ = input('Ты должен выиграть ;)\n==>  ').lower()
            if finish_answ == word:
                break

print('Ну что-ж, давай сыграем в виселицу  ;)')
print('_' * 40)
sleep(1)
play(get_word())
