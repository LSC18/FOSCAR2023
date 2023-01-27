from itertools import combinations

N,M = map(int,input().split())
town = [list(map(int, input().split())) for _ in range(N)]
ans = 1000000
house = []
kfc = []

for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            house.append([i,j])
        elif town[i][j] == 2:
            kfc.append([i,j])

for k in combinations(kfc, M):
    total = 0
    for ho in house:
        dist = 1000000
        for i in range(M):
            dist = min(dist, abs(ho[0] - k[i][0]) + abs(ho[1] - k[i][1]))
        total += dist
    ans = min(ans, total)

print(ans)