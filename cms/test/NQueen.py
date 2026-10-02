# branch4 // level4
# vertical=[j]
# seven=[i+j]
# five=[i-j+n]

n=int(input()) #체스판의 크기
vertical=[0]*n
seven=[0]*(n*2)
five=[0]*(n*2)

cnt=0
def abc(level):
    global cnt
    if level==n:
        cnt += 1
        return

    for j in range(n):
        if vertical[j]==1: continue
        if seven[level+j]==1 or five[level-j+n]==1: continue    #가지치기
        vertical[j], seven[level+j],five[level-j+n]=1,1,1
        abc(level+1)
        vertical[j], seven[level + j], five[level - j + n] = 0,0,0  #백트래킹 개녕

abc(0)
print(cnt)