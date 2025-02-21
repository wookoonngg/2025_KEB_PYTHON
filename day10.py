import time
import random


def bubble_sort(a_list):
    list_length = len(a_list)-1
    for i in range (list_length):
        for j in range (list_length - i):
            if a_list[j] > a_list[i]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        return a_list

# 시간 복잡도 O(n제곱) for문 하나당 O(n) 중첩이라 제곱'


def insertion_sort (list):
    for i in range(1, len(list)):
        value = list[i]
        while i> 0 and list[i-1] > value:
            list[i] = list [i-1]
            i = i-1
        list[i]=value
    return list



import time
import random

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper


@time_decorator
def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        while i > 0 and l[i-1] > value:
            l[i] = l[i-1]
            i = i - 1
            #print(i, end=' ')
        l[i] = value
    return l


@time_decorator
def bubble_sort(l):
    for i in range(len(l) - 1):
        no_swap = True
        for j in range(len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j+1], l[j]
                no_swap = False
                #print(j, end=' ')
        if no_swap:
            return l
    return l


def quick_sort(l):
    n = len(l)
    if n<=1: return l
    pivot = l[n//2]
    left, right = list(), list()
    left, mid, right = list(), list(), list()

    for i in l:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)

    return quick_sort(left)+[pivot]+quick_sort(right)
    return quick_sort(left)+mid+quick_sort(right)


# lists = [4, 55, 55, 7, 55, 9, 11]
# print(quick_sort(lists))

lists1 = [random.randint(1, 100000) for _ in range(10000)]
lists2 = lists1.copy()
lists3 = lists1.copy()
bubble_sort(lists1)
insertion_sort(lists2)

s = time.time()
quick_sort(lists3)
e = time.time()













