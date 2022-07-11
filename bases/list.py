# l1 = []

# # print(l1)
# l1.append(1)
# # print(l1)
# l1.extend([2, 3, 9, 2, 4, 6, 5, 3, 43, 592, 122, 33, 2])
# # print(l1)
# # l1.extend({'a':1,'b':2})
# # print(l1)

# l1.insert(0, 333)
# l1.insert(len(l1), 333)
# l1.remove(1)

# l1.pop()
# l1.pop(1)
# # print(l1.index(3))
# # print(l1.count(3))
# l1.sort()
# l1.sort(reverse=True)
# l1.reverse()
# # l1.clear()
# l1.append({'a': 'abc'})
# l2 = l1.copy()
# print(l2)
# print(l1)
# l1[len(l1)-1]['a'] = "bcd"
# l1.insert(0, 10000)
# print(l2)
# print(l1)
# from collections import deque
# l3 = [1, 2, 3, 4]
# l4 = deque(l3);
# l4.append(5)
# l4.popleft()
# print(l4)

# l5 = list(range(0, 10))
# print(l5)

# l6 = list(map(lambda x: x**2, l5))
# l7 = [x**2 for x in range(10)]
# # print(l6)
# # print(l7)
# # l8 = [(x, y) for x in range(10) for y in range(20) if x != y]
# # print(l8)
# l8 = [x*y for x in range(10) for y in range(20)]
# print(l8)
# l9 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# l10 = [[row[i] for row in l9] for i in range(len(l9)+1)]
# l11 = list(zip(*l9));
# print(list(zip(*l11)))
# l12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # del l12[2]
# del l12[2:10:2]
# del l12[:]
# print(l12)

# for row in l9:
#     l = []
#     for i in range(4):
#         l.append(row[i])
#     print(l)

# for i in range(4):
#     l = []
#     for row in l9:
#         l.append(row[i])
#     print(l)
# list1 = [];
# list2 = [1,2,'3']
# list3 = [i for i in range(1,4)]
# list4 = list()
# list5 = list(range(1,4))
# list6 = list({'a':1,'b':2})
# list2[2:]=[4]
# print(list2)
# print(list1)
# print(list2)
# print(list3)
# print(list4)a
# print(list5)
# print(list6)

# l1=[2, 3, 9, 2, 4, 6, 5, 3, 43, 592, 122, 33, 2]
# l1.sort()
# print(l1)
# l2 = [{'a': 45646}, {'a': 1235}, {'a': 135}, {'a': 822}, {'a': 558}, {'a': 5}]
# l2.sort(key=lambda v: v['a'],reverse=True)

# print(l2)
# l = [1,2,3,4,5,6,7,8,9]

# squs = [];
# for i in range(0,10):
#     squs.append(i**2)
# print(i)
# print(squs)
# print(i)
# l = [i**2 for i in range(10) if i % 3 == 0]
# print(l)
# l = [x*y for x in ['a', 'b', 'c'] for y in [1, 2, 3]]
# print(l)
# l = []
# for x in ['a', 'b', 'c']:
#     for y in [1, 2, 3]:
#         l.append(x*y)
# print(l)

l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = [[row[i] for row in l] for i in range(4)]
print(result)



