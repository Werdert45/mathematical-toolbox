
# Coordinates
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]


# Step size in Gradient Descent
k = 0.1


# Check whether it is possible
if len(x) == len(y):
    print(True)

else:
    print(False)

# Initial values

a = 0
b = 0


def linearFunction(theta):
    v = a*theta+b
    return v


def costFunction():
    m = len(x)
    output = 0
    for i in range(m):
        func1 = (linearFunction(x[i]) - y[i])**2
        output = (1/2*m)*func1
    return output

def aDeriv():
    m = len(x)
    aDer = 0
    for i in range(m):
        func2 = linearFunction(x[i]) - y[i]
        aDer = (1 / m) * func2
    return aDer

def bDeriv():
    m = len(x)
    bDer = 0
    for i in range(m):
        func3 = (linearFunction(x[i]) - y[i])*x[i]
        bDer = (1/m)*func3
    return bDer

def aChange():
    a_new = a-k*aDeriv()
    return a_new

def bChange():
    b_new = b-k*bDeriv()
    return b_new

# Now that it repeats the process and gives the new a and b to the function to retry

# Here this function add all of the functions in here
