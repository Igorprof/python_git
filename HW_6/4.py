class Car:
    def __init__(self, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        print('Car is going to go')
    def stop(self):
        print('Car has been stopped')
    def turn(self, direction):
        print(f'Car turned {direction}')
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, False)
    def show_speed(self):
        if self.speed > 60:
            self.dam = 'Превышение скорости!'
        else:
            self.dam = ''
        print(f'{self.speed} {self.dam}')
    

class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, False)

class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, False)
    def show_speed(self):
        if self.speed > 40:
            self.dam = 'Превышение скорости!'
        else:
            self.dam = ''
        print(f'{self.speed} {self.dam}')

class PoliceCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, True)
