import timeit as tit
import math as m
import time as t

#! this is the fibonacii number done in O(1) time complexity , by Kiritocode1
def timer (f):
    a = t.time()
    for i in range(100):
        print(f(i))
    return print(f"time -> {a-t.time()}")

@timer
def Craby_patty_secret_formula(n):
    invroot5 = 1/m.sqrt(5)
    ax1 = ((1+m.sqrt(5))/2)**n
    ax2 = ((1-m.sqrt(5))/2)**n
    return int(invroot5*(ax1-ax2))
