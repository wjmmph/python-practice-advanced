#REMEMBER:
#keys can be of any immutable type
#and even tuple' elements are required to be immutable if tuple is as a key

my_dict = {"name" : "Kelly", "age": 20, "city": "Sentosa"}
if "city" in my_dict:
    print(my_dict["city"])