datei = open("text.txt", "r")
for _ in datei:
    print(_,end = '')

print(datei.tell())
datei.close()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
import pickle
dd = {1: 'q', 2: [1, 2, 3], 'w': 'Eine Zeichenkette'}
datei = open('meinedatei.txt', 'w')
pickle.dump(dd, datei)
datei.close()

def gen(n):
  z = n
  while True:
    yield z
    z -= 1

x = gen(30)
for key in thisdict:
    print(next(x))
    print(thisdict[key])
for value in thisdict.values():
    print()
    print(value)