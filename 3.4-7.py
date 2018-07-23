# 3.4
name_list = ['Marry', 'John', 'Mack']
print(name_list[0]+" "+name_list[1]+" "+name_list[2])

# 3.5
old = 'John'
new = 'Jack'
print(old+" can't come")
name_list.remove(old)
name_list.append(new)
print(name_list[0]+" "+name_list[1]+" "+name_list[2])

# 3.6
add0 = 'Lucy'
add1 = 'Black'
add2 = 'White'
print("I get a new table")
name_list.insert(0, add0)
name_list.insert(2, add1)
name_list.append(add2)
print(name_list[0]+" "+name_list[1]+" "+name_list[2]+" "+name_list[3]+" "+name_list[4]+" "+name_list[5])

# 3.7
print("I can only invite two person")
popped = name_list.pop(-1)
print("I'm sorry "+popped)
popped = name_list.pop(-1)
print("I'm sorry "+popped)
popped = name_list.pop(-1)
print("I'm sorry "+popped)
popped = name_list.pop(-1)
print("I'm sorry "+popped)

print(name_list[0]+' '+name_list[1])
del name_list[0]
del name_list[0]
print(name_list)
