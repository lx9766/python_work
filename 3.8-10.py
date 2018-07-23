# 3.8
places = ['Qingdao', 'Beijing', 'Wuhan', 'Xian', 'Chongqing']

print('原始列表')
print(places)

print('sorted列表')
print(sorted(places))

print('再次打印原始列表')
print(places)

print('字母相反顺序的sorted')
print(sorted(places, reverse=True))

print('再次打印原始列表')
print(places)

print('reverse列表')
places.reverse()
print(places)
print('再次打印原始列表')
print(places)

print('再次reverse列表')
places.reverse()
print(places)
print('再次打印原始列表')
print(places)

print('打印sort列表')
places.sort()
print(places)
print('打印原始列表')
print(places)

print('打印sort反字母列表')
places.sort(reverse=True)
print(places)
print('打印原始列表')
print(places)


print('列表长度为：'+str(len(places)))
