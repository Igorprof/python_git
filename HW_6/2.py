class Road:
    mas = 1
    sloy = 2
    def __init__(self, w, l):
        self._width = w
        self._length = l
    
    def mass(self):
        return self._width*self._length*Road.mas*Road.sloy


r = Road(7, 5000)

print(r.mass())

