direction = int(input('Шифрование(1) или Дешифрование(2) : '))
lengue = int(input('Английский(1) или Русский(2) : '))
stepue = int(input('Шаг сдвига : '))


def dir1(leng, step):
    text = input('Введите текст : ')
    for i in range(len(text)):
        if 32 <= ord(text[i]) <= 64:
            print(text[i], end='')
        elif leng == 1 and 97 <= ord(text[i]) <= 122 and ord(text[i]) + step > 123:
            c = ((ord(text[i]) + step) - 122) + 96
            print(chr(c), end='')
        elif leng == 1 and 65 <= ord(text[i]) <= 90 and ord(text[i]) + step > 91:
            c = ((ord(text[i]) + step) - 90) + 64
            print(chr(c), end='')
        elif leng == 2 and 1072 <= ord(text[i]) <= 1103 and ord(text[i]) + step > 1103:
            c = ((ord(text[i]) + step) - 1103) + 1071
            print(chr(c), end='')
        elif leng == 2 and 1040 <= ord(text[i]) <= 1071 and ord(text[i]) + step > 1071:
            c = ((ord(text[i]) + step) - 1071) + 1039
            print(chr(c), end='')
        else:
            d = ord(text[i]) + step
            print(chr(d), end='')


def dir2(leng, step):
    text = input('Введите шифр : ')
    for i in range(len(text)):
        if 32 <= ord(text[i]) <= 64:
            print(text[i], end='')
        elif leng == 1 and 97 <= ord(text[i]) <= 122 and ord(text[i]) - step < 97:
            c = (-(ord(text[i]) - step) + 97) + 122
            print(chr(c), end='')
        elif leng == 1 and 65 <= ord(text[i]) <= 90 and ord(text[i]) + step < 65:
            c = (-(ord(text[i]) - step) + 65) + 90
            print(chr(c), end='')
        elif leng == 2 and 1072 <= ord(text[i]) <= 1103 and ord(text[i]) - step <= 1071:
            c = ((-(ord(text[i]) - step)) + 1072) + 1102
            print(chr(c), end='')
        elif leng == 2 and 1040 <= ord(text[i]) <= 1071 and ord(text[i]) - step < 1040:
            c = ((-(ord(text[i]) - step)) + 1040) + 1070
            print(chr(c), end='')
        else:
            d = ord(text[i]) - step
            print(chr(d), end='')
        if c > 90:
            print((c - 90) + 65)


if direction == 1:
    dir1(lengue, stepue)
elif direction == 2:
    dir2(lengue, stepue)
