# 일반 재귀로 짜다가 포기 -> 구글링을 통해 풂.
# https://velog.io/@weenybeenymini/%EB%B0%B1%EC%A4%80-16637%EB%B2%88-%EA%B4%84%ED%98%B8-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0

import sys
input = sys.stdin.readline
result = -987654321

n = int(input())
s = input()

def myOperator(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2

def dfs(index, val):
    global result

    if index ==  n-1:
        result = max(result, val)
        return

    if index + 2 < n:
        dfs(index + 2, myOperator(val, s[index + 1], int(s[index + 2])))

    if index + 4 < n:
        dfs(index + 4, myOperator(val, s[index + 1], myOperator(int(s[index + 2]), s[index + 3], int(s[index + 4]))))
 
dfs(0, int(s[0]))
print(result)
