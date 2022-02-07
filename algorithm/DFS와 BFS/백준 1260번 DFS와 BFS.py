from collections import deque

N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호

graph = {}  # key = parent_node, value = child_nodes_array

for i in range(1, N + 1):  # 모든 노드들 key 설정
    graph[i] = []

for _ in range(M):
    node1, node2 = map(int, input().split())  # parent, child
    graph[node1].append(node2)
    graph[node2].append(node1)


def BFS(graph, start_node):
    passed = [start_node]  # 방문한 노드 저장
    q = deque([start_node])  # 방문할 노드를 저장할 큐 자료형
    while q:  # 모든 노드를 방문할 때 까지 반복
        cur_node = q.popleft()  # 큐에서 첫 번째로 방문할 노드 제거 및 변수에 할당
        for node in sorted(graph[cur_node]):  # 같은 가중치의 자식 노드는 오름차순으로 방문
            if node in passed:  # 이미 방문했던 노드는 되돌아감
                continue
            else:  # 방문하지 않은 노드
                q.append(node)  # 큐에 저장
                passed.append(node)  # 방문 체크
    return passed  # 방문한 순서 반환


def DFS(graph):
    for node in sorted(graph[dfs_stack[-1]]):
        if node not in dfs_passed:
            dfs_stack.append(node)
            dfs_passed.append(node)
            DFS(graph)
    else:
        dfs_stack.pop()


dfs_passed = [V]
dfs_stack = [V]

DFS(graph)
print(*dfs_passed)  # "*": 목록들을 풀어서 표시
print(*BFS(graph, V))
