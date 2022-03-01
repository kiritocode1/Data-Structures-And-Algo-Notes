import timeit as tit
import math as m
import time as t

#! this is the fibonacii number done in O(1) time complexity , by Kiritocode1


def timer(f):
    a = t.time()
    f(1000)
    return print(f"time -> {a-t.time()}")


def timer2(f):
    a = t.time()
    f(1000)
    return print(f"time -> {a-t.time()}")


@timer
def listway(n):
    a = [0, 1]
    b = 0
    c = 1
    for i in range(n):
        sum = a[b]+a[c]
        a.append(sum)
        b += 1
        c += 1

@timer2
def Craby_patty_secret_formula(n):
    # -((1-m.sqrt(5))/2)**n
    return int(1/m.sqrt(5)*(((1+m.sqrt(5))/2)**n))


