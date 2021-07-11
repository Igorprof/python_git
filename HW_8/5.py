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

add_equip(warehouse, [Scanner(5200, 5, 3, ''), Printer(12000, 4, 3, 'inkjet', 'ink'), Printer(10000, 3, 2, 'inkjet', 'ink')])
add_equip(warehouse, [Xerox(2000, 2, 2, 'one-type'), Xerox(3000, 3, 2, 'two-type')])
add_equip(warehouse, [Scanner(5200, 5, 3, ''), Printer(22000, 5, 5, 'inkjet', 'ink')])

groups = send_to_groups(warehouse)

print(groups)
