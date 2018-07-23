motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')  # 末尾添加元素
print(motorcycles)

motorcycles.insert(1, 'bucati')  # 插入元素
print(motorcycles)

del motorcycles[1]  # 直接删除元素
print(motorcycles)

popped_motorcycle = motorcycles.pop()  # 弹出最后一个值，并使用它。只要添加索引就可以pop出任意位置的值
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('yamaha')  # 按照值删除元素
print(motorcycles)



