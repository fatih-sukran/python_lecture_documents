##############################################################


def TowerOfHanoi(n , source, destination, auxiliary): 
    if n==1: 
        print ("Move disk 1 from source",source,"to destination",destination) 
        return
    TowerOfHanoi(n-1, source, auxiliary, destination) 
    print ("Move disk",n,"from source",source,"to destination",destination) 
    TowerOfHanoi(n-1, auxiliary, destination, source) 

n = 5
TowerOfHanoi(n,'C','A','B')


##############################################################


def factorial(n):
    if n == 1 or n == 0:
        print("{}! = {}".format(n,1))
        return 1
    print("{}! = {} * {}!".format(n,n,n-1))
    return n * factorial(n-1)

n = 5
a = factorial(n)
print("The factorial of", n, "is", a)


##############################################################


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib = fibonacci(n-2) + fibonacci(n-1)
    return fib

n = 12
print("Fibonacci Sequance : ")
for i in range(1, n + 1):
    print(fibonacci(i))


##############################################################