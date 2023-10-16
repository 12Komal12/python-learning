year = int(input("Enter the Year:-"))

if (year % 4 == 0) and (year% 100 != 0):
    print("Yes,It's a Leap Year")

elif (year % 400 == 0) and (year% 100 != 0):
    print("Yes,It's a Leap Year")

else:
    print("Not a leap year")