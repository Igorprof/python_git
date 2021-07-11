class Cell:
    def __init__(self, k):
        try:
            self.k = int(k)
        except ValueError:
            print('Количество должно быть числом(целым)')
            self.k = -1
    def __add__(self, other):
        return Cell(self.k + other.k)
    def __sub__(self, other):
        dif = self.k - other.k
        if dif > 0:
            return Cell(dif)
        else:
            print('Разница отрицательна')
    def __mul__(self, other):
        return Cell(self.k * other.k)
    def __truediv__(self, other):
        return Cell(round(self.k / other.k))
    def make_order(self, k_r):
        s = ''
        for i in range(self.k):
            s += '*'
            if (i+1) % k_r == 0:
                s += r'\n'
        return s


c1 = Cell(8)
c2 = Cell(4)
c3 = c1 * c2
print(c3.make_order(5))