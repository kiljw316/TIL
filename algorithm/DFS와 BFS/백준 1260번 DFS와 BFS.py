N, M, V = map(int, input().split())  # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호

graph = {}

for _ in range(M):
    node1, node2 = map(int, input().split())
    if not graph.get(node1):
        graph[node1] = [node2]
    else:
        graph[node1].append(node2)
        
    if not graph.get(node2):
        graph[node2] = [node1]
    else:
        graph[node2].append(node1)
print(graph)


def BFS(graph, start_node):
    from collections import deque
    passed = []
    q = deque([start_node])
    while q:
        cur_node = q.popleft()
        passed.append(cur_node)
        for node in sorted(graph[cur_node]):
            if node in passed:
                break
            else:
                q.append(node)
    return passed


print(*BFS(graph, 1))
