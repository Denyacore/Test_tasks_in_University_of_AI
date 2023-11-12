def main(a, b):
    for i in range(a, b):
        first_condition = i % 11
        if first_condition == 0:
            second_condition = i % 5
            if second_condition != 0:
                print(i)


main(300, 431)