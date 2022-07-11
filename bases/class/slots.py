
from types import MethodType


class Person:
    __slots__ = ('name','age','height','weight')
    def __init__(self, name, age) -> None:
        self.name = name


xm = Person('小明', 18)
# print(xm.name)


# def getName(self):
#     return lambda: self.name

# xm.getName = getName(xm)
# print(xm.getName())

def setName(self, name):
    self.name = name


# xm.setName = setName
# print(xm.setName(xm,'xiaoming'))
# print(xm.name)

# xm.setName = MethodType(setName,xm)
# xm.setName('xiaoming')
# print(xm.name)


# Person.set_name = setName
# xm.set_name('小名')

# print(xm.name)

# xq = Person('xiaoq',30)
# print(xq.name)
# xq.set_name('晓强')
# print(xq.name)

# xm.color = 'white'
xm.height = '150cm'
print(xm.name)

