#You receive a dictionary of students and their scores:
#scores = {    "Aman": 85,    "Riya": 92,    "Kabir": 76,    "Sara": 92,    "Dev": 68}

#Write a program that:
#1. Finds the highest score.
#2. Returns the names of all students who achieved that score.
#3. Stores those names in a list.
#4. Creates a set of all distinct scores.
#Don't assume that only one student can have the highest score.

scores = {    "Aman": 85,    "Riya": 92,    "Kabir": 76,    "Sara": 92,    "Dev": 68}
maxscore = 0

#1. A.
for i, j in scores.items():
    if j > maxscore:
        maxscore = j

#1. B.
lst = scores.values()
maxscore = max(lst)

#2. ; 3.
names = []
for name, marks in scores.items():
    if maxscore == marks:
        names.append(name)

#4. 
distmarks = set(lst)


#OPTIMISED version
scores = {"Aman": 85, "Riya": 92, "Kabir": 76, "Sara": 92, "Dev": 68}

maxscore = max(scores.values())
names = [name for name, marks in scores.items() if marks == maxscore]
distinct_scores = set(scores.values())

print(maxscore)         # 92
print(names)            # ['Riya', 'Sara']
print(distinct_scores)  # {85, 92, 76, 68}