def f(d):
    remaining_cars = []
    for car in d:
        if (car[1] == "in"):
            remaining_cars.append(car[0])
        else:
            remaining_cars.remove(car[0])
    remaining_cars.sort()
    return remaining_cars
