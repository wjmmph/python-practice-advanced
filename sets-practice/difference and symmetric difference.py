#all three methods don't modify the original set in place
setA = {1, 2, 4, 8, 12, 19}
setB = {3, 5, 8, 17, 19}

diff= setA.difference(setB)
print(diff)

diff2 = setB.difference(setA)
print(diff2)

#Symmetric difference: return set with all the elements except those in intersection
symdiff = setA.symmetric_difference(setB)
print(symdiff) #vice verse is also the same