class Date:
    _day = 0
    _month = 0
    _year = 0

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def from_string(cls, data):
        return Date(data[0:data.index('-')],
                    data[data.index('-') + 1: data.index('-', data.index('-') + 1)],
                    data[data.index('-', data.index('-') + 1) + 1: len(data)])

    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        day = int(data[0:data.index('-')])
        month = int(data[data.index('-') + 1: data.index('-', data.index('-') + 1)])
        year = int(data[data.index('-', data.index('-') + 1) + 1: len(data)])
        if 13 > month > 0:
            if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32:
                return True
            if month in [4, 6, 9, 11] and 0 < day < 31:
                return True
            if month == 2:
                if year % 4 == 0 and day < 30 or year % 4 != 0 and day < 29:
                    return True
        return False

    def __str__(self) -> str:
        return 'День: {day}	Месяц: {month}   Год: {year}'.format(day=self._day,
                                                                 month=self._month,
                                                                 year=self._year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))