import random

divisibleBy7 = [n for n in range(1,1001) if n % 7 == 0]
print(divisibleBy7)

w="   hurr  durr"
numberOfSpaces = len([s for s in w if s ==' '])
print(numberOfSpaces)
stuff=("hi", 4, 8.99, "apple", ("t,b","n"))
indexAndValue = [(index, item) for index, item in enumerate(stuff)]
print(indexAndValue)
list_a = [1, 2, 3, 4]
list_b = 2, 3, 4, 5
commonElements = [a for a in list_a
                    for b in list_b if a==b]
print(commonElements)

#v1
numbers = [random.randint(0,1000) for r in range(1000)]
print(len(numbers))
indexAndValueDivisibleBy2 = [(index, value) for index, value in enumerate(numbers) if index % 2 == 0 and value %2 == 0]
indexAndValueDivisibleBy2v2 = [(i,numbers[i]) for i in range(len(numbers)) if i % 2 == 0 and numbers[i] %2 == 0]
print(indexAndValueDivisibleBy2)
print(indexAndValueDivisibleBy2v2)