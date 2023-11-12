def multiplication_table():
    while True:
        number = input('Введите целое число от 1 до 9: ')
        if number.isdigit():
            number = int(number)
            if number > 9:
                print('Число больше 9!')
            elif number < 1:
                print('Число меньше 1!')
            else:
                for i in range(1, 10):
                    result = number * i
                    print(number, 'x', i, '=', result)
                break
        else:
            print('Неверный ввод')


multiplication_table()
