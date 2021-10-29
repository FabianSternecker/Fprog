

date = input("Input date DD/MM/YYYY\n")
date = date.split("/");
date = [int(i) for i in date]
tage = ["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"]
if date[1]<3:
    date[1] += 12
    date[2] -= 1

h = (date[2]//100)
j = (date[2]%100)
w = date[0]
w = w + ((date[1]+1)*26)//10
w = w + (5*j)//4
w = w + h//4
w = w - 2*h - 1
w = w % 7


print(tage[w])