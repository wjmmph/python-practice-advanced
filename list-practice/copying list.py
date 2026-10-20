#there are two types we are going to discuss: 
#1. list copy on place and can modify the original list
#2. list only coopy, and can not modify the original list, and it has three ways to do

original_list = ["apple", "banana", "cherry"]

#1. 
newlist = original_list   
newlist.append("watermelon") #change in newlist would also modify the original list
print(newlist)
print(original_list)

#2.
original_list = ["apple", "banana", "cherry"]
#change in newlist would NOT modify the original list in any of the three cases

#method 1.
newlist1 = original_list.copy()
newlist1.append("watermelon") 
print(newlist1)
print(original_list)

#method 2.
newlist2 = original_list[:]
newlist2.append("watermelon") 
print(newlist2)
print(original_list)
#method 3.

newlist3 = list(original_list)
newlist3.append("watermelon") 
print(newlist3)
print(original_list)