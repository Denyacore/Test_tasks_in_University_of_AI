def car(distance, city):
    fuel_price = 53
    highway_consumption = 5.5 / 100
    city_consumption = 8 / 100

    if city == 0:
        fuel_spent = distance * highway_consumption
    elif city == 1:
        fuel_spent = distance * city_consumption
    else:
        print('данные не верны')

    trave_price = fuel_spent * fuel_price
    print(f"{'*' * 30}\n"
          f"\nпотрачено {round(fuel_spent, 1)} литров бензина\n"
          f"поездка стоила {round(trave_price, 2)} рублей \n"
          f"\n{'*' * 30}")


car(7, 1)
