"""
Yo
"""
from datetime import datetime

runstart = datetime.now()

dc = {}
dc["uno"] = 1
dc["dos"] = 2
dc["tres"] = 3
dc["cuatro"] = 4
dc["cinco"] = 5
dc["seis"] = 6
dc["siete"] = 7
dc["ocho"] = 8
dc["nueve"] = 9
dc["diez"] = 10
print(dc)
dc_original = dc.copy()
# repeatedly asking user for an update
us1 = input("\n\nWant to update your dictionary? Search for an entry:\n")
if us1 in dc:
    print(us1, " is already in the dictionary. Everything up to date.")
elif us1 not in dc:
    dc[us1] = int(input("This is a new 'key'. Assign a 'value' to your entry:\n"))
    print(us1, " has been added to the dictionary")

us1 = input("\n\nWant another update of your dictionary? Search for an entry:\n")
if us1 in dc:
    print(us1, " is already in the dictionary. Everything up to date.")
elif us1 not in dc:
    dc[us1] = int(input("This is a new 'key'. Assign a 'value' to your entry:\n"))
    print(us1, " has been added to the dictionary")

us1 = input("\n\nWant a last update of your dictionary? Search for an entry:\n")
if us1 in dc:
    print(us1, " is already in the dictionary. Everything up to date.")
elif us1 not in dc:
    dc[us1] = int(input("This is a new 'key'. Assign a 'value' to your entry:\n"))
    print(us1, " has been added to the dictionary")
# printing the original and the modified version of the dictionary
print("\nThis is your original dictionary:\n", dc_original)
print("This is your updated dictionary:\n", dc)

runend = datetime.now()
print("\n\nI am done!")
print("Starting time: ", runstart)
print("Ending time: ", runend)
