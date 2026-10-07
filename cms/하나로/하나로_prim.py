import sys
import heapq
sys.stdin = open("re_sample_input.txt","r")

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    x=list(map(int, input().split()))
    y=list(map(int, input().split()))
    rate=float(input())

    visited=[0]*N
    heap=[]

    heapq.heappush(heap,(0,0))
    result=0
    cnt=0

    while heap:
        distance, now = heapq.heappop(heap)
        if visited[now]==0:
            visited[now]=1
            result+=distance
            cnt+=1

        if cnt==N:
            break

        for next in range(N):
            if visited[next] ==0:
                distance=(
                    (x[next]-x[now])**2
                    +(y[next]-y[now])**2
                )
                heapq.heappush(heap, (distance,next))
    result=round(result*rate)

    print(f"#{tc} {result}")