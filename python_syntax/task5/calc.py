def calculator():
    def check_valid_number_a():
        while True:
            user_a = input('Введите первое число: ')
            if user_a.count('.') == 1:
                user_a = float(user_a)
                return user_a
            elif user_a.isdigit():
                user_a = int(user_a)
                return user_a
            else:
                print('Неверный ввод')

    def check_valid_number_b():
        while True:
            user_b = input('Введите второе число: ')
            if user_b.count('.') == 1:
                user_b = float(user_b)
                return user_b
            elif user_b.isdigit():
                user_b = int(user_b)
                return user_b
            else:
                print('Неверный ввод')

    a = check_valid_number_a()
    b = check_valid_number_b()

    def calculating():
        while True:
            user_action = input('Введите действие из разрешенных + - * / : ')
            if user_action == '+':
                result = a + b
            elif user_action == '-':
                result = a - b
            elif user_action == '*':
                result = a * b
            elif user_action == '/':
                if b != 0:
                    result = a / b
                else:
                    print('Ошибка деления на ноль!')
                    continue
            else:
                print('Неверный ввод действия')
                continue
            return result

    calculating()


calculator()
