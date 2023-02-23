import random
import re


def show_field(f):
    print(" ", *[i for i in range(len(f))])
    for i in range(len(f)):
        print(str(i), *f[i])


def input_cors(f):
    while True:
        user_input = input("Введите координаты (x y) через пробел:")
        if not re.match(f'^[0-{n - 1}] [0-{n - 1}]$', user_input):
            print("неверные координаты")
            show_field(field)
        else:
            x, y = map(int, user_input.split())
            if f[x][y] != '-':
                print('поле занято')
                show_field(field)
                continue
            else:
                return x, y


def is_won(f):
    for i in range(n):
        row = []
        column = []
        diagonal1 = []
        diagonal2 = []
        for j in range(n):
            row.append(f[i][j])
            column.append(f[j][i])
            if i == 0:
                diagonal1.append(f[j][j])
                diagonal2.append(f[(n - 1) - j][j])
        a = [row, column, diagonal1, diagonal2]
        if any((len(set(x)) == 1 and '-' not in x) for x in a):
            return True


def zero_bot(f):
    bot_phraze = ('глупый кожаный мешок!', 'сдавайся, тебе не победить суперкомпьютер!', 'Access denied',
                  'лучше бы ты борщ варил!', 'Нас reboot, а мы крепчаем.', 'Меньше знаешь – реже виснешь.')
    while True:
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        if f[x][y] == '-':
            print('zero_bot:', random.choice(bot_phraze))
            return x, y


# крестики-нолики для любого размера поля n x n
# input для n пропущен, чтобы проще было проверять
# n = int(input('Введите размер поля (n): '))
n = 3
field = [['-' for i in range(0, n)] for j in range(0, n)]
show_field(field)
counter = 0
while counter < n ** 2:
    # строка для тестирования - бот против бота
    # x, y = zero_bot(field) if counter % 2 == 0 else zero_bot(field)
    x, y = input_cors(field) if counter % 2 == 0 else zero_bot(field)
    field[x][y] = 'x' if counter % 2 == 0 else 'o'
    show_field(field)
    counter += 1
    if is_won(field):
        print(f'Победили {field[x][y]}-ки!')
        break
    elif counter == n ** 2:
        print("Ничья!")
