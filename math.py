import math

n = int(input("Zadej celé kladné číslo: "))
print("Faktoriál", n, "je", math.factorial(n))

if n > 1:
    for i in range (2, n):
        if (n % i) == 0:
            print(n, "není prvočíslo.")
            break
    else:
        print(n, "je prvočíslo.")
else:
    print(n, "není prvočíslo.")

x = 1
y = 1
z = x + y
z1 = z
z2 = y
if n == 1:
    print(x)
elif n == 2:
    print (x, y, end=" ")
else:
    print(x, y, z, end=" ")
    for i in range (n-3):
        z = z1 + z2
        z2 = z1
        z1 = z
        print (z, end=" ")