from collections import deque

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx,ny))
    return cnt

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

paper = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paper.append(bfs(graph, i ,j))

if len(paper) == 0:
    print(len(paper)) # 그림의 개수
    print(0)
else:
    print(len(paper))
    print(max(paper)) # 가장 넓은 그림의 넓이