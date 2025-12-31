working=int(input("Total number of working days: "))
absent=int(input("Total number of days of absent: "))

Percentage=(working - absent) / working * 100
print("Your precentage is", Percentage)

if Percentage <= 75:
    print("You are not allowed to attend the exam.")
else:
    print("You are allowed to attend the exam.")