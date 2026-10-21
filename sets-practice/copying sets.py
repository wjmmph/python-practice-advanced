setA = {1, 2, 3, 4, 5, 6}

#way 1
setB = setA
setB.add(9)
print(setA) #setA also get modified

#way 2: no modification in original set
#method 1: 
setC = setA.copy()

#method 2:
setD = set(setA)
