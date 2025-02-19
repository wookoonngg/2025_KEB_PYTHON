# class Stack:
#     def __init__(self):
#         self.items = list()
#
#     def push(self, data):
#         self.items.append(data)
#
#     def pop(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#     def peek(self):
#         return self.items[-1]
#
#     def is_empty(self):
#         return len(self.items) ==0
#
#     s1 = Stack()
#     s1.push(-9)
#     s1.push(11)
#     s1.push(977)
#

# class Node:
#     def __init__(self, data, next=None):
#         self.data =data
#         self.next = next
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     def append (self,data):
#       if not self.head:
#         self.head = Node (data)
#         return
#       current = self.head
#       while current.next:
#           current = current.next
#         current.next = Node(data)
#
#     def reverse_list(self):
#         current = self.head
#         previous =None


# class Node:
#     def __init__(self, data, next=None):
#         self.data=data
#         self.next = next
#
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self._size =0
#
#     def enqueue(self, item):
#         self._size +=1
#         node = Node(item)
#         if self.rear is None:
#             self.front = node
#             self.rear =node
#         else:
#             self.rear.next = node
#             self.rear = node
#
#     def dequeue(self):
#         if self.front is None:
#             raise IndexError('pop from empty queue')
#         self._size-= 1
#         temp = self.front
#         self.front = self.front.next
#         if self.front is None:
#             self.rear = None
#         return temp.data
#
#     def size(self):
#         return self._size


# 큐가 모두 찼을 때의 경우를 코드로 작성해서 true 리턴해야됨 각 케이스 별로
# t/f로 판별하고 난 다음 공간을 확보해야 입력이 되니까 그거 까지 처리



# def is_queue_full() :
#     global rear, front
#
#     if rear != size - 1: # rear가 front 쪽에 가서 뒤에 공간이 남은 경우임
#         return False
#     elif (front == -1) and (rear == size-1): # front [0][1][2][3] rear 인 경우 를 말하는거임 즉 완전히 꽉 찬 경우
#         return True
#     else:
#         for i in range (front+1, size):
#             queue[i-1] = queue[i]
#             queue[i] = None
#
#         front = front - 1
#         rear = rear -1
#
#         return False


def is_queue_full():
    global rear, front, queue, size

    if (rear + 1) % size






def is_queue_empty() :
    global size, queue, front, rear
    if front == rear:
        return True
    else :
        return False


def en_queue(data) :
    global size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def de_queue() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front+1]


size = int(input("큐의 크기를 입력 : "))
queue = [None for _ in range(size)]
front = rear = -1

if __name__ == "__main__" :
    while True:
        menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
        if menu == 'X' or menu == 'x':
            break
        elif menu== 'E' or menu == 'e' :
            data = input("입력할 데이터 : ")
            en_queue(data)
            print(queue)
        elif menu== 'D' or menu == 'd' :
            print("삭제된 데이터 : ", de_queue())
            print(queue)
        elif menu== 'P' or menu == 'p' :
            print("확인된 데이터 : ", peek())
            print(queue)
        else:
            print("입력이 잘못됨")
    print("프로그램 종료!")