# year = 2016
# event = 'Referendum'
# s=f'Results of the {year} {event}'
# # print(s)

# s1= '{}Results of the{}'.format(year,event)
# print(s1)

# s2 = 'asdgas'
# i2 = 123
# print(s2+str(i2))
# print(repr(i2))
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:6} ==> {phone:10}')

s3 = '{} and {}'.format('gg', 'ww')
s3 = '{0} and {1}'.format('gg', 'ww')
s3 = '{0} and {0}'.format('gg', 'ww')
s3 = '{1} and {1}'.format('gg', 'ww')
s3 = '{1} and {0}'.format('gg', 'ww')
# print(s3)
s4 = '{ww} and {gg}'.format(gg='gg', ww='ww')
s4 = '{0} and {gg}'.format('hh', gg='gg', ww='ww')
# print(s4)
for i in (range(100)):
    print('{0:4} {1:4} {2:4}'.format(i, i**2, i**3))
