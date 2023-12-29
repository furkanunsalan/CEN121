from question_1_car import Car

def solution():
    car = Car(2019, "Tesla")
    
    for i in range(5):
        car.accelerate()
        print(car.get_speed())

    for i in range(5):
        car.brake()
        print(car.get_speed())

solution()
