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

class Xerox:
    def __init__(self, price, size, guarantees, type_):
        super().__init__(price, size, guarantees)
        self.type_ = type_
        
scan = Scanner(8500, 10, 3, '')        
print(scan.__dict__)