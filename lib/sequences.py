#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    for n in range(length) :
        if(n < 2) :
            fib.append(n)
        else :
            fib.append(fib[n-1] + fib[n-2])
    print(fib)
