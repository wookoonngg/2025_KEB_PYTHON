
# 요세푸스 알고리즘 without linked , 큐

num = int(input("사람 명수를 입력하세요: "))
k = int(input("k를 입력하세요: "))

# num이 사람 수 링으로 생각했을 때 k번째 수 애를 죽임

arr = [i + 1 for i in range(num)]  # 1부터 시작하는 리스트 생성

# num이 7개에 k가 3일 때라고 가정
# 죽으면 -1로 표시하자 살아있으면 안에 숫자 그대로 리턴

# 바깥 반복문에서 모든 배열의 값이 (하나 빼고) -1가 될 때까지 돌림  / 걍 남은 사람 수 변수 한개 더 만들어서 하는게 나을듯
# arr[0]에서 시작해서 i+3 = x ,  i+3+3 = x , 여기서 if i+3+3이 num 보다 크면 다시 arr[0] 부터 돌려야함

i = 0  # 처음 시작 arr[0]
remain = num
# 남은 사람 수

while remain > 1:  # 한 명만 살아있을 때까지

    count = 0

    while count < k:
        if arr[i] != -1:  # -1 아닌 경우 살아있는 놈 찾음
            count += 1

        if count == k:
            break  # k 번째 애 만나면 num 나머지로 감
        i = (i + 1) % num

    arr[i] = -1
    remain -= 1  # 죽은 사람 카운트 세어야 함

    while arr[i] == -1:
        i = (i + 1) % num

# 마지막 출력
print(arr)






























# import time
# import random
#
#
# def bubble_sort(a_list):
#     list_length = len(a_list)-1
#     for i in range (list_length):
#         for j in range (list_length - i):
#             if a_list[j] > a_list[i]:
#                 a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
#         return a_list
#
# # 시간 복잡도 O(n제곱) for문 하나당 O(n) 중첩이라 제곱'
#
#
# def insertion_sort (list):
#     for i in range(1, len(list)):
#         value = list[i]
#         while i> 0 and list[i-1] > value:
#             list[i] = list [i-1]
#             i = i-1
#         list[i]=value
#     return list
#
#
#
# import time
# import random
#
# def time_decorator(func):
#     def wrapper(*arg):
#         s = time.time()
#         r = func(*arg)
#         e = time.time()
#         print(f'실행시간 : {e - s}초')
#         return r
#     return wrapper
#
#
# @time_decorator
# def insertion_sort(l):
#     for i in range(1, len(l)):
#         value = l[i]
#         while i > 0 and l[i-1] > value:
#             l[i] = l[i-1]
#             i = i - 1
#             #print(i, end=' ')
#         l[i] = value
#     return l
#
#
# @time_decorator
# def bubble_sort(l):
#     for i in range(len(l) - 1):
#         no_swap = True
#         for j in range(len(l) - 1 - i):
#             if l[j] > l[j+1]:
#                 l[j], l[j + 1] = l[j+1], l[j]
#                 no_swap = False
#                 #print(j, end=' ')
#         if no_swap:
#             return l
#     return l
#
#
# def quick_sort(l):
#     n = len(l)
#     if n<=1: return l
#     pivot = l[n//2]
#     left, right = list(), list()
#     left, mid, right = list(), list(), list()
#
#     for i in l:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#
#     return quick_sort(left)+[pivot]+quick_sort(right)
#     return quick_sort(left)+mid+quick_sort(right)
#
#
# # lists = [4, 55, 55, 7, 55, 9, 11]
# # print(quick_sort(lists))
#
# lists1 = [random.randint(1, 100000) for _ in range(10000)]
# lists2 = lists1.copy()
# lists3 = lists1.copy()
# bubble_sort(lists1)
# insertion_sort(lists2)
#
# s = time.time()
# quick_sort(lists3)
# e = time.time()
#
#
#










