#COPY methods: there are two types in which: 1. original would be modified on place 2. original won't be modified
#2. has two ways
my_dict = {"name" : "Kelly", "age" : 28, "email" : "kelly143W@xyz.com"}

#1. on place modification if copy get changed
my_dict_cpy = my_dict
my_dict_cpy["city"] = "Sentosa"
print(f"Copy: {my_dict}\nOriginal: {my_dict_cpy}")

#2.
my_dict_cpy2 = my_dict.copy() #WAY A
my_dict_cpy3 = dict(my_dict)  #WAY B
del my_dict_cpy2["city"]
del my_dict_cpy3["name"]

print(f"Copy 1: {my_dict_cpy2}\nCopy 2: {my_dict_cpy3}\nOriginal: {my_dict_cpy}")