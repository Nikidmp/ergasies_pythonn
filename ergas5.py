import random
import math

M = 0
F = 0
x = 0
y = 0
pinakas = []
while x < 3 or y < 3:
    x = int(input("Δώσε το μήκος του πίνακα : "))
    y = int(input("Δώσε το πλάτος του πίνακα : "))

th: int = (x * y)
n = th / 2
m = math.ceil(n)

for w in range(100):
    M = []
    pin = []
    k = 0

# κατασκευάζω μια λίστα απο λίστες,κάθε μια απο τις οποίες περιέχει μια γραμμή του πίνακα

    for i in range(x):
        P = []
        for j in range(y):
            P.append("O")
        pin.append(P)

    i = 0
    while i < m:
        z = random.randint(0, th - 1)
        row = z // y
        col = z % y
        if pin[row][col] == "O":
            pin[row][col] = "S"
            i += 1


    for i in range(0, x):  # οριζόντια
        for j in range(0, y - 2):
            w = pin[i][j] + pin[i][j + 1] + pin[i][j + 2]
            if w == "SOS":
                F = F + 1
                k += 1


    for j in range(0, y):  # κάθετα
        for i in range(0, x - 2):
            g = pin[i][j] + pin[i + 1][j] + pin[i + 2][j]
            if g == "SOS":
                F = F + 1
                k += 1

    for i in range(1, x - 1):  # διαγώνια
        for j in range(1, y - 1):
            if pin[i][j] == "O":
                if (pin[i - 1][j - 1] == "S" and pin[i + 1][j + 1] == "S") or (
                        pin[i + 1][j - 1] == "S" and pin[i - 1][j + 1] == "S"):
                    F = F + 1
                    k += 1
    #print(F)
    print(k)

    for s in pin:
        print(*s)
print(F)
M = F / 100
print("Ο μέσος όρος εμφάνισης των SOS είναι: ", M)