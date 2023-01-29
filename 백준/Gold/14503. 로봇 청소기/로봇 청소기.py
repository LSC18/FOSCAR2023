N, M = map(int, input().split())
x, y, d = map(int, input().split())

visited = [[0] * M for _ in range(N)]

dx = [-1,0,1,0] 
# 북(0)쪽을 바라볼 때 왼쪽의 x좌표값은 -1, 동(1)쪽을 바라볼 때 왼쪽의 x좌표값은 0...
dy = [0,1,0,-1]
# 북(0)쪽을 바라볼 때 왼쪽의 y좌표값은 0, 동(1)쪽을 바라볼 때 왼쪽의 y좌표값은 1...

field = [list(map(int, input().split())) for _ in range(N)]

visited[x][y] = 1
cnt = 1

while True:
    flag = 0
    for i in range(4):
        d = (d + 3) % 4
        # direction = 3 - direction 보다 명확한 식
        #왼쪽으로 한칸 돌리면 0,1,2,3 -> 3,2,1,0이 됨.
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                x = nx
                y = ny
                cnt += 1
                flag = 1
                break
    if flag == 0: # 사방이 청소 불가일 떄
        if field[x-dx[d]][y-dy[d]] == 1:
            print(cnt)
            break
        else:
            x = x-dx[d]
            y = y-dy[d]