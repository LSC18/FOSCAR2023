import sys
import heapq # 우선순위 큐

input = sys.stdin.readline
N = int(input())
cls = []
for i in range(N):
    a, b = map(int, input().split())
    cls.append([a, b])

cls.sort() # 각 강의의 시작 시간을 기준으로 정렬

queue = []
heapq.heappush(queue, cls[0][1]) # 첫 강의의 끝나는 시간 저장

for i in range(1, N):
    if cls[i][0] < queue[0]: # 기존 강의가 끝나는 시간보다 이를 때
        heapq.heappush(queue, cls[i][1]) # 새 강의실 추가
    else: # 기존 강의가 끝나는 시간보다 같거나 이후일 때
        heapq.heappop(queue) # 기존 강의 시간 pop
        heapq.heappush(queue, cls[i][1]) # 새 강의 시간 추가

print(len(queue))