N = input()
PA = []

for i in range(len(N)):
    PA.append(N[i])

stk = []
cnt = 0
while cnt < len(N):
    stk.append(PA[cnt])
    cnt += 1
    if len(stk) >= 4:
        if stk[-1] == 'P' and stk[-2] == 'A' and stk[-3] == 'P' and stk[-4] == 'P':
            stk.pop()
            stk.pop()
            stk.pop()

if len(stk) == 1 and stk[0] == "P":
    print("PPAP")
else:
    print("NP")