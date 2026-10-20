my_dict = {"name" : "Max", "age" : 28, "city" : " Boston"}

#deletion method
#1. 
del my_dict["name"]
print(my_dict)

my_dict["name"] = "Kelly"
my_dict["email"] = "kelly143W@xyz.com"

#2.
my_dict.pop("age")
print(my_dict)

#3. Arbitrary for python version <7 and last element inserted for >=7
my_dict.popitem()
print(my_dict)
