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
