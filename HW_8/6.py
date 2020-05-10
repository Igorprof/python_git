class Equipment:
    def __init__(self, price, size, guarantees):
        self.price = price
        self.size = size
        self.guarantees = guarantees

class Printer(Equipment):    
    def __init__(self, price, size, guarantees, type_, ink_supply):
        super().__init__(price, size, guarantees)
        self.type_ = type_
        self.ink_supply = ink_supply

class Scanner(Equipment):    
    def __init__(self, price, size, guarantees, type_):
        super().__init__(price, size, guarantees)
        self.type_ = type_

class Xerox(Equipment):
    def __init__(self, price, size, guarantees, type_):
        super().__init__(price, size, guarantees)
        self.type_ = type_


        
def add_equip(wh, items):
    wh.extend(items)

def send_to_groups(wh):
    gr = {}
    for item in wh:
        name = item.__class__.__name__
        if name in gr:
            gr[name] += 1
        else:
            gr[name] = 1
    return gr    

warehouse = []

try:
    print('Первый принтер')
    printer1 = Printer(int(input('Введите цену первого принтера: ')), int(input('Размер: ')), int(input('Гарантия(лет): ')), input('Тип: '), input('Спобоб подачи чернил: '))
    print('Второй принтер')
    printer2 = Printer(int(input('Введите цену второго принтера: ')), int(input('Размер: ')), int(input('Гарантия(лет): ')), input('Тип: '), input('Спобоб подачи чернил: '))
    print('Третий принтер')
    printer3 = Printer(int(input('Введите цену третьего принтера: ')), int(input('Размер: ')), int(input('Гарантия(лет): ')), input('Тип: '), input('Спобоб подачи чернил: '))
    print('Первый сканер')
    scanner1 = Scanner(int(input('Введите цену первого сканера: ')), int(input('Размер: ')), int(input('Гарантия(лет): ')), input('Тип: '))
    print('Второй сканер')
    scanner2 = Scanner(int(input('Введите цену второго сканера: ')), int(input('Размер: ')), int(input('Гарантия(лет): ')), input('Тип: '))
except ValueError:
    print('Ошибка в типе введенных данных!')

add_equip(warehouse, [printer1, printer2, printer3])
add_equip(warehouse, [scanner1, scanner2, printer3])

groups = send_to_groups(warehouse)

print(groups)
