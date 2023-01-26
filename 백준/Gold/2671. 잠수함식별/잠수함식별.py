import re

target = input() #정규표현식은 int가 아니라 str으로 대체시키므로 인퓻 형태 조심
stand = re.compile('(100+1+|01)+') #기준(100~1~|01)~
answer = stand.fullmatch(target) #match fullmatch 차이 확인

if answer:
    print("SUBMARINE")
else:
    print("NOISE")