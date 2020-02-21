#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Jordan"
import sys


def add(x, y):
    return x + y


def multiply(x, y):
    total = 0
    if y < 0:
        for i in range(abs(y)):
            total = add(total, -x)
    else:
        for i in range(y):
            total = add(total, x)
        return total


def power(x, n):
    total = 1
    if x < 0:
        for i in range(n):
            total = multiply(total, abs(x))
        return -total
    else:
        for i in range(n):
            total = multiply(total,x)
    return total


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        for i in range(1, x):
            x = multiply(x, i)
    return x


def fibonacci(n):
    x = [0, 1]
    for i in range(2, n + 1):
        x.append(add(x[i-2], x[i-1]))
    return x[n - 1]

def main():
    option = sys.argv[1]
    if option == 'add':
        print(add(1,2))
        print(add(4,5))
        print(add(-2, -6))
        print(add(-5, 2))
        print(add(10, -2))
    elif option == 'multiply':
        print(multiply(1,2))
        print(multiply(4,5))
        print(multiply(-7,-6)) 
        print(multiply(-4,7))
        print(multiply(8,-6)) 
    elif option == 'power':
        print(power(1,2))
        print(power(4,5))
        print(power(-6,3))
        print(power(6,3))
    elif option == 'factorial':
        print(factorial(0))
        print(factorial(1))
        print(factorial(4))
    elif option == 'fib':
        print(fibonacci(2))
        print(fibonacci(4))
        print(fibonacci(8))
    else: 
        print('unknown option')
if __name__ == '__main__':
    main()
