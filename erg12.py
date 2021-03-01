f = input("dose ena arxeio ascii keimenou: ")
try:
    file = open(f, "r")
except FileNotFoundError:
    print("Το αρχειό δεν βρέθηκε!")
    exit(1)
w = file.read().replace("\n", " ")
w = w[::-1]
print(w)
slist = []
for i in range(0, len(w)):
    k = (ord(w[i]))
    kat = (128 - k)
    n = chr(kat)
    print(n, end="")
    slist.append(n)

print("\n")
print(slist)






