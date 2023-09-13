# Python program for nth fibonacci number.

def fib(n):
    if n<=0:
        return f'fibonacci sequence does not exists for negative numbers.'
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input('Enter any number: '))
print(f'Nth fibonacci number is: {fib(n)}')
