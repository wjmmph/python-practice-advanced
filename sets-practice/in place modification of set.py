setA = {1, 2, 4, 8, 12, 19}
setB = {3, 5, 8, 17, 19}
setA.update(setB)
print(setA) #add all elements from setB to setA which are not present in setA and modify the original set in place


setC = {1, 2, 4, 8, 12, 19}
setD = {3, 5, 8, 17, 19}
setC.intersection_update(setD) #modify setC and remains only the elements which are in intersection of both sets
print(setC) 
#C = C intersection D


setE = {1, 2, 4, 8, 12, 19}
setF = {3, 5, 8, 17, 19}
setE.difference_update(setF)
print(setE) #modify setE and remove all the elements which are in intersection of both sets
#E = E - F


setG = {1, 2, 4, 8, 12, 19}
setH = {3, 5, 8, 17, 19}
setG.symmetric_difference_update(setH)
print(setG) #addition of difference update by vice verse
#G = (G - H) intersection (H - G)