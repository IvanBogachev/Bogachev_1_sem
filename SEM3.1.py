def Fib(n):
    if n < 3 :
        return 1

    else:
        return Fib(n-1) + Fib(n-2)





print(Fib(10))