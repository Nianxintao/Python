number = [13, 2, 5, 98, 56 ]
print(number)
print(number[3])
number [2] = 85
print(number)

# 添加data （从数列尾部添加）
number.append(42)
print(number)

# 在数列中任何位置添加data 第一个数字表示 index num；第二个数字表示添加的data）
number.insert(2, 16)
print(number)

#  删除data（从数列尾部删除）
number.pop()
print(number)

# 删除指定data（不是index 是指定的数字）
number.remove(2)
print(number)

# 从小到大排列
number.sort()
print(number)

# 反向排列数列
number.reverse()
print(number)

# 显示数列中data的数量
print(len(number))

#  空行 \n 为一行
print("\n\n\n\n")
#  Tuple - 也是数据列 但是不可以被编辑 不要被替换的数据 使用
names = ("John", "Jane", "Mile")

print(names)
print(names[1])

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "...")

