def leap_year_check():
    while True:
        user_input = int(input('Введите год от 1900 до 3000 в формате YYYY:'))
        if user_input >= 1900 and user_input <= 3000:
            if (
               user_input % 400 == 0 or
               user_input % 4 == 0 and user_input % 100 > 0
               ):
                print('Високосный')
            else:
                print('Обычный')
            break
        else:
            print('Введенный год выходит за требуемый диапазон')


leap_year_check()
