
from functools import reduce

# def triangles(max):
#     result = [1]
#     for x in range(1, max):
#         print(result)
#         result.append(1)
#         for y in range(1, x):
#             result[x-y] = result[x-y-1]+result[x-y]

def triangles(max):
    result = [1]
    for x in range(1, max):
        print(result)
        print(list(map(lambda x: x**2, result)))
        print(reduce(lambda x, y: x+y, result))
        result.append(0)
        for y in range(x, 0, -1):
            result[y] = result[y-1]+result[y]


triangles(11)
