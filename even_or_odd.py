# list all num from 1 to 100, and state whether odd or even

list_even = []
list_odd = []

for i in range(1, 101):
    if i %2 == 0:
        list_even.append(i)
        # print(f" {i} is even")
    else:
        list_odd.append(i)
        # print(f"{i}is odd")
print(f"Even list {list_even}")
print("\n\n")
print(f"Odd list {list_odd}")