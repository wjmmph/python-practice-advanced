#set methods
myset = set()

#1. add
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(5)

#2. remove
myset.remove(3) #3 is removed from the set
# myset.remove(6)   as 6 is not in set
# keyerror: 

#3. discard
myset.discard(3) #as 3 is already removed, it do nothing and return the set as it is
myset.discard(1) #1 is removed
#myset here is now {2, 4, 5}

#4. pop: arbitrary removal and return of that value
print(myset.pop())

#5. clear: empty our set
myset.clear()

