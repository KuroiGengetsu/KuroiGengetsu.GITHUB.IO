"""Define a function to figure out Fibonacci numbers"""

def Fibonacci(num):
    """Use recursion 同figure out Fibonacci"""
    if num == 1 or num == 2:
        return 1
    elif num > 2:
        return Fibonacci(num - 1) + Fibonacci(num - 2)

if __name__ == '__main__':
    print(Fibonacci(13)) # this will print 233.

