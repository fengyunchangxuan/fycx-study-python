import time
import functools

# def now():
#     timestamp = time.time()
#     print(timestamp)
# # now()
# # print(now.__name__)


# def log(func):
#     def call(*args, **kw):
#         print('call %s' % func.__name__)
#         return func(*args, **kw)
#     return call

# @log
# def now():
#     timestamp = time.time()
#     print(timestamp)

# # f = log(now)
# # f()
# now()

def log(text):
    def deco(func):
        @functools.wraps(func)
        def call(*args, **kw):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return call
    return deco


@log('gg')
def now():
    timestamp = time.time()
    print(timestamp)


now()

# def now():
#     timestamp = time.time()
#     print(timestamp)

# f = log('ggww')(now)
# f()
print(now.__name__)
