class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


p1 = Position('Ivan', 'Ivanov', 'profi', {'wage':10000, 'bonus':20000})

print(p1.name)
print(p1.surname)
print(p1.get_full_name())
print(p1.get_total_income())