import math

def my_pow(b,e):
    if e <0:
        b = 1/b
        e = e*-1

    result = 1

    i = int (e)
    f = e-i


    for _ in range(i):
        result = result * b

    if f >0:
        result = result * math.exp(f*math.log(b))

    return result


print(my_pow(10, -2))
print(my_pow(2, 9))
print(my_pow(16, 0.5))
print(my_pow(10, 3))
print(my_pow(25, 0.5))

