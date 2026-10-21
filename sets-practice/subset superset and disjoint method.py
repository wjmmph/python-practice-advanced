setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

#issubset: -> bool
print(setA.issubset(setB)) #False
print(setB.issubset(setA)) #True

#issuperset: -> bool (exactly opposite of subset, it check whether first set contain all the elements of other set)
print(setA.issuperset(setB)) #True
print(setB.issuperset(setA)) #False

#isdisjoint: -> bool (if intersection is null set) (vice verse is same)
print(setA.isdisjoint(setB)) #False 

setC = {7, 8, 9, 10}
print(setA.isdisjoint(setC)) #True