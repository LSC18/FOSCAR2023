bar = input()
stk = []
ans = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stk.append('(')
    else:
        if bar[i-1] == '(':
            stk.pop()
            ans += len(stk)
        else:
            stk.pop()
            ans += 1
print(ans)