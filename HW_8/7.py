class Complex:
    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im
    def __str__(self):
        return f"{self.re}{'+' if self.im > 0 else ''}{self.im}i"
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im + other.re*self.im)

c1 = Complex(4, 4)
c2 = Complex(3, -6)

print(c1 + c2)
print(c1 * c2)
