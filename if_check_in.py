mylist = list(range(9))
check = 5
check2 = 18
if check in mylist:
    print("blubb")
if check2 not in mylist:
    print("not blubb")

menu1 = ["gluten", "peanuts", "lactose", "people"]
menu2 = ["gluten", "meat", "my_immune_system"]
check1 = input(
    "\nWhat are you allergic to? Enter up to three things and I will recommend a menu\n"
)
check2 = input("What else are you allergic to? \n")
check3 = input("What else are you allergic to? \n")

if check1 in menu1 and check1 in menu2:
    print("I recommend you look for another restaurant")
elif check1 in menu1 and check1 not in menu2:
    print("I recommend menu 2")
elif check1 in menu2 and check1 not in menu1:
    print("I recommend menu 1")

if check2 in menu1 and check2 in menu2:
    print("I recommend you look for another restaurant")
elif check2 in menu1 and check2 not in menu2:
    print("I recommend menu 2")
elif check2 in menu2 and check2 not in menu1:
    print("I recommend menu 1")

if check3 in menu1 and check3 in menu2:
    print("I recommend you look for another restaurant")
elif check3 in menu1 and check3 not in menu2:
    print("I recommend menu 2")
elif check3 in menu2 and check3 not in menu1:
    print("I recommend menu 1")
