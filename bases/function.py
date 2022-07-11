
# def fib(max):
#     list = []
#     a, b = 0, 1
#     while a < max:
#         list.append(a)
#         c=a
#         a += b
#         b=c
#     else:
#         return list
# # fib(100)

# print(fib(20000))

# i = 5


# def f(arg=i):
#     print(arg)
#     print(i)


# i = 6
# f()

# def f1(a,L=[]):
#     L.append(a)
#     return L;

# print(f1(1))
# print(f1(2))
# print(f1(3))
# print(f1(4))
# print(f1(5))
# def f2(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L


# # print(f2(1))
# # print(f2(2))
# # print(f2(3))
# # print(f2(4))
# # print(f2(5))

# print(f2(L=[1], a=2))
# def f3(a,*b,**c):
#     print(a)
#     print(b)
#     print(c)

# # f3(1)
# # f3(1,2)
# # f3(1,2,3)
# f3(1,2,3,name='小白',age='12345')

# def f4(x,y,/,z,*w):
#     print(x)
#     print(y)
#     print(z)
#     print(w)

# f4(1,2,3,4,5,6)

# def f4(*,x,y):
#     print(x)
#     print(y)
# f4(x=1,y=2)

# def f5(name,/, **kwds):
#     return 'name' in kwds

# f5(1,name="2")

# def f6(*args,sep=","):
#     print(sep.join(args))
#     return sep.join(args)

# f6('1','2','3','4')
# f6('1','2','3','4')

# print(range(5))
# print(list(range(5)))
# l1 = [1,6]
# print(list(range(*l1)))
# print(*l1)

# def f7(n):
#     return lambda x:x+n;

# f8=f7(100);
# print(f8(10))

# l2 = [(4, 'four'), (2, 'two'), (3, 'three'), (1, 'one')]
# l2.sort(key=lambda v: v[0])
# print(l2)
# l2.sort(key=lambda v: v[1])
# print(l2)

# def f9():
#     """ Nothing!
#     nobody
#     """
#     return

# print(f9.__doc__)

# def f10(x: str, y: int) -> str:
#     return x*y

# print(f10('12345',20))
# print((1+2)*3)
# print(f10.locals())

# def f11():
#     a=10;
#     print(locals())
#     return

# print(f11())

# def func1(x, y=2, z=3):
#     return x + y + z

# # print(func1(1))
# # print(func1(1,2))
# # print(func1(1,2,3))


# print(func1(10,100,j=100)) #

# def f3(x, y, /):
#     return x+y


# print(f3(1, 2))
# print(f3('a', 'b'))

# print(f3(1, x=2))

# def f4(*, x, y):
#     return x+y

# print(f4(x=1, y=2))
# print(f4(1,2))

def f5(x, /, y, *,z):
    return x+y+z
# print(f5(1, 2, z=3))
print(f5(x=1, y=1, z=3))

