
# class Animal:
#     age = 20
#     # love = [1,2,3]

#     def __init__(self, name, color, type, son) -> None:
#         self.name = name
#         self.color = color
#         self.type = type
#         self.son = son

#     def info(self):
#         print(self.name)
#         print(self.color)
#         print(self.type)
#         print(self.age)
#         # print(self.love)
#         print(self.son)


# xiaobai = Animal('小白', 'white', 'cat', ['a'])
# xiaohei = Animal('小黑', 'black', 'cat', ['2'])
# # print(xiaobai)
# # print(xiaobai.name)
# # print(xiaobai.color)
# # print(xiaobai.type)
# # xiaobai.age = 1;
# # xiaobai.love[0] = '1000'
# # xiaobai.son[0] = 'son'
# # xiaobai.info();
# # xiaohei.info();


# class Cat(Animal):
#     def __init__(self, name, color, son) -> None:
#         super().__init__(name, color, 'cat', son)


# xiaolv = Cat('小绿', 'green', ['xiaobai', 'xiaohua'])
# # print(xiaolv)
# # xiaolv.info()
# # print(isinstance(xiaolv,Animal))
# # print(isinstance(xiaolv,Cat))
# # print(issubclass(Cat,Animal))
# # print(issubclass(bool,int))

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def getInfo(self):
        print('我叫 {0} , 我今年 {1} 岁,我的身高是 {2} cm，我的体重是 {3} kg'.format(
            self.name, self.age, self.height, self.weight))


xiaoming = Person('小明', '18', '180', '60')
xiaoming.getInfo()
