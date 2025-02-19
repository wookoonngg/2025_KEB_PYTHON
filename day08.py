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

#
# def is_queue_full():
#     global rear, front, queue, size
#
#     if (rear + 1) % size
#
#
#
#
#
#
# def is_queue_empty() :
#     global size, queue, front, rear
#     if front == rear:
#         return True
#     else :
#         return False
#
#
# def en_queue(data) :
#     global size, queue, front, rear
#     if is_queue_full():
#         print("큐가 꽉 찼습니다.")
#         return
#     rear += 1
#     queue[rear] = data
#
# def de_queue() :
#     global size, queue, front, rear
#     if is_queue_empty():
#         print("큐가 비었습니다.")
#         return None
#     front += 1
#     data = queue[front]
#     queue[front] = None
#     return data
#
# def peek() :
#     global size, queue, front, rear
#     if is_queue_empty():
#         print("큐가 비었습니다.")
#         return None
#     return queue[front+1]
#
#
# size = int(input("큐의 크기를 입력 : "))
# queue = [None for _ in range(size)]
# front = rear = -1
#
# if __name__ == "__main__" :
#     while True:
#         menu = input("삽입(E)/삭제(D)/확인(P)/종료(X) : ")
#         if menu == 'X' or menu == 'x':
#             break
#         elif menu== 'E' or menu == 'e' :
#             data = input("입력할 데이터 : ")
#             en_queue(data)
#             print(queue)
#         elif menu== 'D' or menu == 'd' :
#             print("삭제된 데이터 : ", de_queue())
#             print(queue)
#         elif menu== 'P' or menu == 'p' :
#             print("확인된 데이터 : ", peek())
#             print(queue)
#         else:
#             print("입력이 잘못됨")
#     print("프로그램 종료!")



class TreeNode:
    def __init__(self):
        self.left =None
        self.right = None
        self.data = None


if __name__ == "__main__":
    groups =['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이','트와이스']
    root = None


# 리스트에 있는 값들을 순차적으로 트리에 삽입하는 코드
# 상위 노드랑 비교해서 걔보다 작으면 왼쪽으로 크면 오른쪽으로 가는 -> 한글도 순서대로 크기 비교 가능함
# root가 블랙핑크가 되고 while문에서 레드벨벳 ㄹ이 ㅂ보다 작으니까 블핑 왼쪽 아래로 정렬 -> 첫번째 if문에 해당
# 마마무 ㅁ은 ㅂ보다작으니 일단 외쪽으로 근데 왼쪽아래가 레드벨벳으로 none이 아니니까 근데 레벨 ㄹ보단 크니까 레벨 오른쪽 아래로 ->첫번째 if문의 else에 해당

    node = TreeNode()
    node.data = groups[8]
    root =node

    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left =node
                    break
                current = current.left

            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right



    find_group = input()

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이 존재하지 않습니다")
                break
            current = current.data


    deleteName = input()


    current = root
    parent = None
    while True:
        # 지우고자 하는 애가 현재 데이터랑 같은 경우 즉 지울 애를 찾았을 때
        if deleteName == current.data:

            # 근데 지우고자 하는 애가 자식이 없느 경우
            if current.left == None and current.right == None:
                if parent.left == current:
                    parent.left = None
                else :
                    parent.right = None
                del (current)


            # 자식이 왼쪽에 붙어있는 경우
            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right =current.left
                del(current)

            # 지우려고 하는 애가 오른쪽에 자식이 있는경우
            elif current.right != None and current.left == None:
                if parent.right == current:
                    parent.right = current.right
                else:
                    parent.left =current.right
                del(current)

            print(deleteName, '이(가) 삭제됨.')
            break

            # 지우려고 하는 애가 자식이 둘다 있을 때
            else:
                successor = current.right
                successor_parent = current
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

            # 더 작은 노드 값을 현재 노드 current로 들고옴
                current.data = successor.data

            # 오른쪽 애 삭제 , 왜 더 작은애니까
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right

            print(deleteName, "이(가) 삭제됨.")

        else:
            print(deleteName, "이 트리에 없음")




