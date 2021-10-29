li =[lambda x: x+n for n in range(10)]

result = [j(10) for j in li]

print(result)

li2 = [lambda k: lambda x: k+x(n) for n in range(10)]

result = [j(10) for j in li2]

print(result)
