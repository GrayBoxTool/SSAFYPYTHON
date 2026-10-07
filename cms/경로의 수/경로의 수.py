import sys
sys.stdin=open("test_in.txt","r")

def dfs(now):
    global cnt
    if now==G:
        cnt+=1
        return 

    for to in range(1,N+1):
        if edges[now][to]==1 and visited[to]==0:
            visited[to]=1
            dfs(to)
            visited[to]=0

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    edges=[[0]*(N+1) for _ in range(N+1)]
    nums=list(map(int,input().split()))
    for i in range(M):
        edges[nums[i*2]][nums[i*2+1]]=1
    S,G=map(int,input().split())
    cnt=0
    stack=[S]
    visited=[0]*(N+1)
    visited[S]=1
    dfs(S)
    print(f"#{tc} {cnt}")