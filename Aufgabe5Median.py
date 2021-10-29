import math
numbers = []
for x in range(1,6):
   numbers.append(input("Enter number %d\n"%x))

numbers.sort()
n = len(numbers)
if n%2==0:
   print((numbers[(n//2)-1]+numbers[(n//2)])/2)
else:
   print(numbers[((n+1) // 2)-1])
