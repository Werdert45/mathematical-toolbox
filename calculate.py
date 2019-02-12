from constants import e, pi

"""
print("LOGb(X)")
x = int(input("Give x  "))
base = int(input("Base: "))
"""

# Tools:


def factorial(num):

    fact = 1
    for i in range(1, num+1):
        fact = fact*i

    return fact



# Functions of growth:


def log(base, x):

    for variable in range(0, 8):

        n = 0
        whileword = 2
        while whileword > 0:
            if base**n <= x:
                n += 1
            else:
                n -= 1
                digit = n
                print(digit)
                break

        y = x/(base**n)
        x = y**10


def ln(x):

    for variable in range(0, 8):
        n = 0
        whileword = 2
        while whileword > 0:
            if e**n <= x:
                n += 1
            else:
                n -= 1
                digit = n
                print(digit)
                break
        y = x/(e**n)
        x = y**10

# Trigonometric functions


def sin(x):

    total = 0
    x = x * pi/180
    for i in range(0, 10):
        sums = (((-1)**i)*(x**((2*i)+1)))/factorial((2*i)+1)
        total = total + sums
    return total


# cosecant funciton for the o/h
def csc(x):
    total = 0
    x = x * pi / 180
    for i in range(0, 10):
        sums = (((-1) ** i) * (x ** ((2 * i) + 1))) / factorial((2 * i) + 1)
        total = total + sums
    return 1 / total


# cosine function, for the a/h


def cos(x):
    x = x * pi / 180
    total = 0
    for i in range(0, 10):
        sum = ((x ** (2 * i)) / factorial(2 * i)) * ((-1) ** i)
        total = total + sum
    return total

# secant function, for the h/a


def sec(x):
    x = x * pi / 180
    total = 0
    for i in range(0, 10):
        sum = ((x ** (2 * i)) / factorial(2 * i)) * ((-1) ** i)
        total = total + sum
    return 1 / total




def tan(x):
    x = x * pi /180
    total = 0
    for i in range(0, 10):
        sum = ((x ** (2 * i + 1)) / factorial(2 * i + 1)) * ((-1) ** i)
        total = total + sum
