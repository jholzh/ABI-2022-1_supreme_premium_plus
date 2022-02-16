"""
This will insert items at a specific position in a list
"""
ls1 = list(range(14))
ls2 = list(range(22))
ls3 = list(range(26))

print(ls1)
print(ls2)
print(ls3)
# We need the user input to determine what we want to add where to which list
in1 = int(input("\nWould you like to add something to these lists? Enter here pls \n"))
in2 = int(input("What list do you want to add something to? [1, 2, 3?]\n"))
in3 = int(input("Where do you want to add that? \n"))

print("You chose to add ", in1, " to list ", in2, " at position ", in3)

if in2 == 1:
    ls1.insert(in3, in1)
elif in2 == 2:
    ls2.insert(in3, in1)
elif in2 == 3:
    ls3.insert(in3, in1)

# Check if the user addition is already part of the list
if in1 in ls1:
    print("Moron! This value is already part of list 1")
elif in1 in ls2:
    print("Moron! This value is already part of list 2")
elif in1 in ls3:
    print("Moron! This value is already part of list 3")
else:
    print("What a great addition!")
# print the altered list
if in2 == 1:
    print(ls1)
elif in2 == 2:
    print(ls2)
elif in2 == 3:
    print(ls3)
# done
print("\n\nI am done!")
