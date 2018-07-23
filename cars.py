# 使用sort永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 永久性排序
print(cars)
cars.sort(reverse=True)  # 字母反顺序排序
print(cars)
# 使用sorted临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

print("Here is the sorted list:")
print(sorted(cars))  # 暂时排序，不改变原顺序

print('Here is the original list again:')
print(cars)

print(sorted(cars, reverse=True))  # 临时字母反向排序

# 用reverse反向打印
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # 反向排序
print(cars)

# len确定表的长度
print(len(cars))
