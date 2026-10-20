mylst = ["apple", "banana", "cherry", "date", "elderberry"]

#method 1: on place reverse
mylst.reverse()
print(mylst)

#method 2: sort + reverse
mylst.sort(reverse = True)
print(mylst)

#method 3: newlist as by product
newlst = sorted(mylst, reverse = True)
print(newlst)

#method 4: using slicing and it also can be done in place or by product
print(mylst[::-1])