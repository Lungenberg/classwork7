"""
class Car():
    color = ''
    wheels = 4
    year_of_manufacture = ''
    move = 100
    mark = ''

    def __init__(self, color, y, m):
        self.color = color
        year_of_manufacture = y
        mark = m

    def SpeedUp(self, a):
        self.move = self.move + a
    def SpeedDown(self, a):
        self.move -= a    # -= Это сокращённая форма

m1 = Car('Blue', 1988, 'KIA')
print(m1.color)
m1.color = 'Red'
m1.year_of_manufacture = 2005
m1.mark = 'Toyota'

print(m1.color)
print(m1.mark)
"""
import print as print


class Student():
    id = ''
    name = ''
    year = ''
    mark = ''

    math = 0
    info = 0
    eng = 0

    def __init__(self, id, name, year, mark):
        self.id = id
        self.name = name
        self.year = year
        self.mark = mark

    def Sum(self, math, info, eng):
        self.math = math
        self.info = info
        self.eng = eng

        sum = ((math + info + eng) / 3)
        print(sum)

    def Info(self):
        print("Name: ", self.name)
        print("Course: ", self.year)
        print("Average Mark: ", self.mark)

    def Master(self, a):
        if (a<9):
            print("Есть возможность поступить на мастерат")
        else:
            print("Нет возможности поступить на мастерат")

Vadim = Student(12345, "Vadim",4, 7)

Vadim.Sum(8,5,9)

