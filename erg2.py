from random import randint

x = int(input("Δώσε έναν ακέραιο αριθμό: "))


def fibo(x):
    i = 1
    j = 1
    for k in range(x - 2):
        tmp = i
        i = i + j
        j = tmp
    return i


y = fibo(x)
print("O", x, "ος όρος της ακολουθίας fibonacci είναι ο", y)

b = 0
for i in range(20):
    a = randint(0, y - 1)
    if pow(a, y, y) != a:
        b = 1

if b == 0:
    print("Ο αριθμός", y, 'είναι πρωτος')
else:
    print("Ο αριθμός", y, 'δεν είναι πρωτος')
