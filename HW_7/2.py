from abc import ABC, abstractmethod

class Clothers(ABC):
    @abstractmethod
    def __init__(self, title, param):
        self.title = title
        self.param = param
    @abstractmethod
    def costs(self):
        print('I am abstract method')
    

class Coat(Clothers):
    def __init__(self, title, V):
        self.title = title
        self.V = V
    def costs(self):
        return self.V/6.5 + 0.5
    @property
    def name(self):
        return self.title

class Costume(Clothers):
    def __init__(self, title, H):
        self.title = title
        self.H = H        
    def costs(self):
        return 2*self.H + 3
    @property
    def name(self):
        return self.title

coat1 = Coat('coat1', 5)
coat2 = Coat('coat2', 25)
coat3 = Coat('coat3', 15)
costume1 = Costume('costume1', 10)
costume2 = Costume('costume2', 20)
costume3 = Costume('costume3', 30)

clothers_list = [coat1, coat2, coat3, costume1, costume2, costume3]

cost = 0
print('costs: ')
for cl in clothers_list:
    print(f'{cl.name} - {round(cl.costs(), 2)}')
    cost += cl.costs()

print(f'general cost: {round(cost, 2)}')

