alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def caesar_encode(src, dist):
    code = ""
    for n in src:
        wasUpper = False
        if n.isupper():
            wasUpper = True
            n = n.lower()
        if n not in alphabet:
            code += n
            continue
        currentIndex= alphabet.index(n)
        encodeIndex = (currentIndex + dist) % len(alphabet)
        if wasUpper:
            code += alphabet[encodeIndex].upper()
        else:
            code += alphabet[encodeIndex]

    return code
def caesar_decode(src, dist):
    return caesar_encode(src,-dist)
print(caesar_encode("HelloFrend",60))
print(caesar_decode(caesar_encode("HelloFrend",60),60))

toCrack = "Ugpco ypvi xb zdbeatii ktglpwgadhitc Ipmx fjtg sjgrw Qpntgc."

for i in range(15,16):
    print(caesar_decode(toCrack,i)+" "+ str(i))

"""
text = input("Enter text\n")
dist = input("Enter distance\n")
print("Enter D for Decode and E for Encode\n")
if input()=="D":
    print(caesar_decode(text,int(dist)))
else:
    print(caesar_encode(text,int(dist)))
"""