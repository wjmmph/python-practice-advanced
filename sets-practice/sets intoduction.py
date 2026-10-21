#sets: unordered, mutable, no duplicates


#METHODS
#1.
myset1= {1, 2, 3}
print(myset1) #output: {1, 2, 3}

myset2 = {1, 2, 3, 2, 1}
print(myset2)  #output: {1, 2, 3}

#2. using function but argument should be an iterable
myset3 = set([1, 2, 3, 2, 1])
myset4 = set("hello") #output: it would be any possible combination of unique characters in the argument

#For empty set
mydict = {} #output pf type(mydict): type dict
newset = set() #type: set

