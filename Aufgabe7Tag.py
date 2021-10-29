def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

months = [31,28,31,30,31,30,31,31,30,31,30,31]
date = input("Input date DD/MM/YYYY\n")
date = date.split("/");
value = int(date[0])
for x in range(1,int(date[1])):
    if isLeapYear(int(date[2])) and x == 2:
        value += months[x]+1
    else:
        value += months[x]


print(str(value)+"th day of the year")