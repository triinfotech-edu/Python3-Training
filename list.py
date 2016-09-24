#!/usr/bin/python

# list

list = [1, 2, 3, 5, 10, 11, 'apple', 3.1415, 'banana', 12.45+78.12j]

list.append(100)
list.remove(11)

print(list)

print(list[1:])

print(list[-3])

list[2] = 99
print(len(list))
print(list)