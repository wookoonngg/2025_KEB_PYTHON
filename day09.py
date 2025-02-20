# class TreeNode:
# 	def __init__(self):
# 		self.left = None
# 		self.data = None
# 		self.right = None
#
#
# def insert(root, value):
#     new_node = TreeNode()
#     new_node.data = value
#
#     if root is None:
#         return new_node
#
#     current = root
#     while True:
#         if value < current.data:
#             if current.left is None:
#                 current.left = new_node
#                 break
#             current = current.left  # move
#         else:
#             if current.right is None:
#                 current.right = new_node
#                 break
#             current = current.right  # move
#     return root
#
#
# def search(root, value):
#     pass
#
#
# def post_order(node):
#     if node is None:
#         return
#     post_order(node.left)
#     post_order(node.right)
#     print(f"{node.data} ", end='')
#
#
# if __name__ == "__main__":
#     numbers = [10, 15, 8, 3, 9]
#     root = None
#
#     for number in numbers:
#         root = insert(root, number)
#
#     print("BST 구성 완료")
#     post_order(root)


    # find_group = int(input())
    #
    # current = root
    # while True:
    #     if find_group == current.data:
    #         print(f"{find_group}을(를) 찾았습니다")
    #         break
    #     elif find_group < current.data:
    #         if current.left is None:
    #             print(f"{find_group}이(가) 존재하지 않습니다")
    #             break
    #         current = current.left
    #     else:
    #         if current.right is None:
    #             print(f"{find_group}이(가) 존재하지 않습니다")
    #             break
    #         current = current.right



class Graph:
	def __init__(self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(name_ary[v], end =' ')
    print()
    for row in range(g.SIZE) :
        print(name_ary[row], end =' ')
        for col in range(g.SIZE) :
            #print("%2d" % g.graph[row][col], end = ' ')
            print(f"{g.graph[row][col]:2}", end=' ')
        print()
    print()

# dfs : 불필요한 간선 삭제하고 각 노드?들이 아직 잘 연결되어 있는지 확인하는 함수 인것같은데
# 스택을활용하여 돌아


# 처음에 current 가 0으로 시작
# 크루스컬 알고리즘

#과제 : dfs를 재귀나 스택을 사용하지 말고 queue 를 사용하여 코드를 작성해보아라
# queue 에 순차적으로 append 하고 queue가 다 정리가 되면 while문 finish


from collections import deque


def dfs (g, current, find_vtx, visited) :
    queue = deque() # 일단 큐를 만들어양함
    visited = [] # 방문한 애들 모아두는 배열 일단 만들긴하는데 아래 만들었는데 또만들어야되나? 전역변수 쓰긴 에바임

    queue.append(start) #시작노드를 걍 current =0 해서 current로 넣는 것도 ㄱㅊ을 지도

    while queue:
        current = queue.pop() # 나중에 들어온게 먼저 나감 그래서 current 값 먼저 pop

        if current not in visited:
           visited.append(current) # 왜 빨간줄이냐 -> 줄맞춤 에러~ ㅅㄱ

        for next in range(len(g[current])): # 이거 반대로 돌려야되나? 몰루 어케 반대로 돌림? 몰루몰루몰루 몰루
            if g[current][next] != 0 and next not in visited:
                queue.append(next)

    return visited # 까먹을뻔~


def find_vertex(g, find_vtx):
    visited = []
    return dfs(g, 0, find_vtx, visited)


# dfs를 활용한 find vertex

# def dfs(g, current, find_vtx, visited):
#     visited.append(current)
#     if current == find_vtx:
#         return True
#     for vertex in range(g.SIZE):
#         if g.graph[current][vertex] != 0 and vertex not in visited:
#             if dfs(g, vertex, find_vtx, visited):
#                 return True
#     return False

# 스택을 활용한 find_vertex함수

    # stack = []
    # visited_ary = []
    #
    # current = 0 # 현재 0부터 돌기 시작
    # stack.append(current) # 스택에 0 노드를 저장
    # visited_ary.append(current) # visited arr 에 0 (서울)을 저장한거다 -> 서울만 일단 방문한 도시가 된거임 하고 밑에 while문 내려가면
    #
    # while len(stack) != 0: # 스택에 모든것이 pop 될 때까지 -> 모든것을 다 돌고 next가 none 된 상태임
    # 	next = None
    # 	for vertex in range(g_size) : # 모든 노드들을 도는데
    # 		if g.graph[current][vertex] != 0 :
    # 			if vertex in visited_ary : # 처음에 0 들어온거는 앞에서 visit에 저장했으니까 여기 if문 pass ->
    # 				pass # 현재 노드가 방문한 지점이라는게 보이면 (스택을 통해 확인하는 것) -> visited arr이면 넘어감
    # 			else :
    # 				next = vertex  # visited arr에 없으면 그 노드가 next 가 됨 -> 바로 밑에 if문에 걸려서 스택,visited arr 에 append
    # 				break
    # 	if next is not None:
    # 		current = next
    # 		stack.append(current)
    # 		visited_ary.append(current)
    # 	else :
    # 		current = stack.pop() # current++; ???
    # if find_vtx in visited_ary :
    # 	return True
    # else :
    # 	return False

# 여기까지 함수 find vtx




G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

g_size = 6
G1 = Graph(g_size)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print_graph(G1)

# 간선 목록 만들기 [가중치, 시작도시, 도착도시]
edge_ary = []
for i in range(g_size) :
	for k in range(g_size) :
		if G1.graph[i][k] != 0 :
			edge_ary.append([G1.graph[i][k], i, k])

print(edge_ary, len(edge_ary))

# 가중치 순으로 목록 정렬 (내림차순)
from operator import itemgetter
edge_ary = sorted(edge_ary, key = itemgetter(0), reverse = True)

print(edge_ary, len(edge_ary))

# 중복 간선 제거
new_ary = []
for i in range(0, len(edge_ary), 2) :
	new_ary.append(edge_ary[i])

print(new_ary, len(new_ary))

index = 0
while len(new_ary) > g_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
	start = new_ary[index][1]
	end = new_ary[index][2]
	saveCost = new_ary[index][0]

	G1.graph[start][end] = 0
	G1.graph[end][start] = 0

	startYN = find_vertex(G1, start)
	endYN = find_vertex(G1, end)

	if startYN and endYN :
		del new_ary[index]
	else :
		G1.graph[start][end] = saveCost
		G1.graph[end][start] = saveCost
		index += 1

print_graph(G1)















