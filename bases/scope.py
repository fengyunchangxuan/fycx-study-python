# for i in range(10):
#     a = 100;
#     print(i)
# print(i)
# print(a)

# while i<100:
#     print(i)
#     i+=1

# num1 = 1;
# def f1():
#     global num1
#     print(num1)
#     num1 = 2
#     print(num1)
# f1()
# def f2():
#     num2 = 2
#     def f3():
#         nonlocal num2
#         print(num2)
#         num2 = 3
#         print(num2)
#     f3()
# f2();


# print(vars())
    # print(abs)
# abs = 1
# num1 = 1
# def f1():
#     num1 = 2
#     def f2():
#         global num1
#         num1 = 3    
#     f2();
#     print(num1)
# f1()
# print(num1)
# print(globals()['num1'])

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
