
month = int(input("Enter month: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

if month * day == year:
    print("It's a magic date")
else:
    print("It's a not magic date")