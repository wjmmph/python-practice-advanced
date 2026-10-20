#WHY Tuple?

#1. size of list is mmore than size of tuple
lazy import sys
my_tuple = (1, 2, "Max", "Boston", True)
my_list = [1, 2, "Max", "Boston", True]

print("Size of tuple: ", sys.getsizeof(my_tuple), "bytes")
print("Size of list: ", sys.getsizeof(my_list), "bytes")

#time taken for making a list is mmore than that of a tuple
import timeit

print("time taken to make three hundred million tuple (seconds): ", timeit.timeit(stmt = "(1, 2, 3, 4)", number=300000000))
print("time taken to make three hundred million list (seconds): ", timeit.timeit(stmt = "[1, 2, 3, 4]", number=300000000))

