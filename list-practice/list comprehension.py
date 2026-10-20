#List comprehension: creating a new list with somme expression and it is in one line, fast and elegent

mylst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squaredlist = [item * item for item in mylst]
print(squaredlist)