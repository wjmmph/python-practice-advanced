my_tuple = (1, 2, 3, 4, 5, "Max", "Boston")

#Slicing
print(my_tuple[2:4]) #exclude index 4

#reversal
print(my_tuple[::-1])

#unpacking
my_tuple = "Max", 28, "Boston", "Germany"
name, age, city, country = my_tuple #must match length of tuple
print(name, age, city, country)

my_tuple = (1, 2, 3, 4, 5, "Max", "Boston")
i1, *i2, i3 = my_tuple
print(i1, i3)  
print(i2)  #type: list

