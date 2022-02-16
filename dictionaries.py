"""
Yo
"""
from datetime import datetime

runstart = datetime.now()

dict = {}
# dict["hello"] = "hola"
# dict["healthy"] = "sano"
# dict["pool"] = "piscina"
# print(dict)
# print(dict.keys())
# print(list(dict.values()))
# print(list(dict.keys()))

# import time
# print(datetime.now())
# time.sleep(3)
dict["Dell"] = 23
dict["Acer"] = 14
dict["Lenovo"] = 8
print(dict)
usr1 = input("Add a value to this dictionary:\n")
key1 = input("Now also add a key to your value:\n")
dict[usr1] = key1
print(dict, "\nThat was easy, wasn't it.")
usr2 = input("Now remove an entry from it:\n")
# while True:
#     input(raw > input)
#     if usr2 in dict:

if usr2 in dict:
    del dict[usr2]
else:
    usr2 = input("Your chosen entry is not part of the dictionary. Try another one:\n")
    del dict[usr2]
print("\nLook what you've done.", dict)

runend = datetime.now()
print("\n\nI am done!")
print("Starting time: ", runstart)
print("Ending time: ", runend)
