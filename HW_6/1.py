from time import sleep

class TrafficLight:
    __color = ('red', 'yellow', 'green')
    def running(self):
        print(TrafficLight.__color[0])
        sleep(7)
        print(TrafficLight.__color[1])
        sleep(2)
        print(TrafficLight.__color[2])
        sleep(5)

s = TrafficLight()

s.running()