class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
    @classmethod
    def datefromstr(cls, str_date):
        try:
            d, m, y = list(map(int, str_date.split('-')))
            if (d is None) or (m is None) or (y is None):
                raise Exception
            return cls(d, m, y)
        except Exception:
            print('Неверный формат даты')        
    @staticmethod
    def isvalid(date):
        try:
            date.day = int(date.day)
            date.month = int(date.month)
            date.year = int(date.year)
        except ValueError:
            return False
        return (1<=date.day<=31) and (1<=date.month<=12)

d1 = Date.datefromstr('01-01-2020')
print(Date.isvalid(d1))
