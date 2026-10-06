import sys
sys.stdin = open("re_sample_input.txt","r")

def findgroup(num):
    if island_num[num]==num:
        return num

    else:
        now_num=findgroup(island_num[num])
        island_num[num]=now_num
        return now_num

def union(a,b):
    parent_a=findgroup(a)
    parent_b=findgroup(b)

    if parent_a==parent_b:
        return
    else:
        if parent_a<parent_b:
            island_num[parent_b]=parent_a
        else:
            island_num[parent_a]=parent_b

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    x=list(map(int,  input().split()))
    y=list(map(int,  input().split()))
    island=[]
    island_num=[]
    bridge=[]
    for i in range(N):
        island.append((x[i],y[i]))
        island_num.append(i)
    rate=float(input())


    for i in range(N):
        for j in range(i,N):
            bridge.append(((i,j),(abs(x[j]-x[i])**2+abs(y[j]-y[i])**2)))

    bridge.sort(key=lambda x : x[1])
    result=0
    cnt=0

    for islands, distance in bridge:
        a,b=islands
        if findgroup(a)!=findgroup(b):
            union(a,b)
            result+=distance
            if cnt==N-1:
                break
    result= round(result*rate)
    print(f"#{tc} {result}")


