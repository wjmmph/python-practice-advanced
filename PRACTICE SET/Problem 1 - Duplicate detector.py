#question: Given this list:

#numbers = [4, 7, 2, 7, 9, 4, 1, 2, 2]

#Write a program that identifies the numbers appearing more than once.
#Requirements:
#- Return each duplicated number only once.
#- Your result must be a set.
#- Do not manually write the answer into your code.
#Think about: How can you detect whether youve already encountered a number?'''

#1.
numbers = [4, 7, 2, 7, 9, 4, 1, 2, 2]
set2 = set()

for i in numbers:
    count = numbers.count(i)
    if count > 1:
        set2.add(i)

print(set2) 
#PROBLEM: O(n**2)


#2.
for i in set(numbers):
    if i in numbers:
        numbers.remove(i)

print(set(numbers))
#PROBLEM: if unique entries are very large in numbers


#3. 
numbers = [4, 7, 2, 7, 9, 4, 1, 2, 2]
seen = set()
duplicates = set()

for n in numbers:
    if n in seen:        
        duplicates.add(n)
    else:
        seen.add(n)      

print(duplicates) 