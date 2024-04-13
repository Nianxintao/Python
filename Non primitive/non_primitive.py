# Non-primitive Data Types

# List - collection of data - mutable(change the data in the list) - indexed

numbers = [ 12, 32, 2, 4, 56, 78 ]
#                        0    1    2   3   4     5

print (numbers)
print(numbers[4])

numbers.append(12)
print(numbers)

numbers[1] = 25
print(numbers)

numbers.pop()
print(numbers)


# Tuples - collection of data - immutable (cannot change) -  indexed
days = ("Monday", "Tuesday", "Wednesday")
#                    0                     1                            2
print(len(days))
print(days)
print(days[1])

# days[2] = "Friday"     - Cannot do this

# days.append("Friday")     - Cannot do this







# sets {} - collection of data - mutable(can change) - not indexed - no repeated items

names = { "John", "Jane", "Mike" }

print(names)

names.add("Smith")
print(names)

names.remove("John")
print(names)

names.add("Jane")    # not display   NOT showing dup data
print(names)

a = { 5, 3, 1, 2, 4 } # { 1, 2, 3, 4, 5 }
b = { 5, 7, 8, 4, 6 } # { 4, 5, 6, 7, 8 }

u = a.union(b) # b.union(a)
print(u)

i = a.intersection(b) # b.intersection(a)
print(i)

dab = a.difference(b) # A - B
print(dab)

dba = b.difference(a) # B - A
print(dba)

print(2 in a)
print(10 in a)

for number in a:
    print(number)

# Dictionary - collection of data - mutable (change) - keyed - key value pair

person1 = {
    "name": "John",
    "surname": "Smith",
    "age": 32
}

print(person1)
print(person1["name"])          # key not indexed
print(person1.get("name"))

# there is difference between print(person1[]) and print(person1.get())
# print(person1["phone"]) if the data not in the dic it will break the code
print(person1.get("phone", "No phone number provided"))   # it will print None or what ever you put in ""

person1["address"] = "Melbourne"       # add  new key and new value
print(person1)
person1["age"] = 40   # change key and value
print(person1)

person1.pop("surname")   # remove key and value
print(person1)

# Loop
for key in person1:
    print(f"{key}")
    print(person1[key])




    persons = [
        {
            "name": "Person1",
            "address":  "Perth"
          },
        {
            "name": "Person2",
            "address": "Melbourne"
        },
        {
            "name": "Person3",
            "address": "sydney"
        },

    ]

    