# class Person:
#     def __init__(self, name, age) -> None:
#         self._name = name
#         self._age = age

#     def set_name(self, name):
#         self._name = name

#     def get_name(self):
#         return self._name

#     def set_age(self, age):
#         if not isinstance(age, int):
#             raise ValueError('score must be an integer!')
#         if age < 0 or age > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = age

#     def get_age(self):
#         return self._age


# xm = Person('小明', 15)
# xm.set_age(200)

class Person:

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        print('getter name = %s' % self._name)
        return self._name

    @name.setter
    def name(self, name):
        print('setter name = %s' % name)
        self._name = name

    @property
    def age(self):
        print('getter age = %s' % self._age)
        return self._age
    
    def __str__(self) -> str:
        return 'Person obejct(name:%s,age:%s)'%(self._name,self._age)
    __repr__ = __str__

    def __iter__(self):
        return self


xm = Person('小明', 18)
# xm.name = '小明'
# print(xm.name)
# xm.age = 25
xm.name = 'xiaoming'

# print(xm.name)
# print(xm.age)
# print(xm)

for item in xm:
    print(item)
