class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')
    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')

class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')
    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')

class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')
    def draw(self):
        print(f'{self.title}. Запуск отрисовки.')

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()