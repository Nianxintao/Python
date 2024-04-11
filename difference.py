# 原始数据 与 非原始数据的区别
num1 = 5  # assign 5 to num1
num2 = num1   # assigned the value of num1 to num2   copies the data by value
num1 = 10  # assign 10 to num1

print(num1)
print(num2)

list1 = [1, 2, 3, 4]  # assign [] to list1
list2 = list1  # assign list1 to list2
list1.append(5)  # change something in list1
print(list1)
print(list2)

#  原始数据在改变num1 赋值后 num2 不改变之前的赋值
#  非原始数据在改变list1 赋值后 list2 也一起改变