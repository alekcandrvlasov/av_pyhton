"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода.
"""


class Date:

    def __init__(self, day=0, mth=0, yer=0):
        self.day = day
        self.mth = mth
        self.yer = yer

    @classmethod
    def cl_date(cls, param):
        day, mth, yer = map(int, param.split('-'))
        date = cls(day, mth, yer)
        return date

    @staticmethod
    def valid(param):
        day, mth, yer = map(int, param.split('-'))
        return day <= 31 and mth <= 12 and yer <= 2020


date1 = Date.cl_date('09-08-2020')
date2 = Date.cl_date('10-08-2020')

print(date2.day, date2.mth, date2.yer)

date3 = Date.valid('10-08-2020')

print(date3)

date4 = Date.valid('10-08-2021')

print(date4)