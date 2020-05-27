import math

# checks if n is a prime number
def Is_number(n):
    try:
        n = int(n)
    except ValueError:
        raise Exception("It has to be a whole number greater than 0.")
    
    if n <= 0:
        raise Exception("The number has to be greater than 0.")
    else:
        return True

# finds a factorial of a number:
def Factorial(n):
    return math.factorial(n)

# checks if n is a prime number
def Is_prime_number(n):
    if n > 1:
        for i in range (2, n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

# calculates n numbers of Fibonacci Sequence
def Fibonacci_sequence(n):
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


n = input("Insert any natural number: ")
try:
    Is_number(n)
except Exception as ex:
    print(ex)
    exit()
    
n=int(n)

prime = Is_prime_number(n)
if prime == True:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

print("Factorial of {} is {}.".format(n, Factorial(n)))

print("{} numbers of Fibonacci Sequence are:".format(n))
Fibonacci_sequence(n)
