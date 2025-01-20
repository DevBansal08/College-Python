day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    month_days[1] = 29  


day += 1

if day > month_days[month - 1]:  
    day = 1
    month += 1


    if month > 12:
        month = 1
        year += 1


print(f"Next Date: day={day} month={month} year={year}")
