import sys
sys.stdin = open("sample_input.txt","r")

def dfs(cnt,now):
    global min_cnt
    if cnt-1 >=min_cnt:
        return
    if now==N:
        min_cnt=min(min_cnt,cnt-1)
        return
    for i in range(L[now],0,-1):
        if now+i<=N:
            dfs(cnt+1, now+i)
        



T=int(input())
for tc in range(1,T+1):
    L=list(map(int,input().split()))
    N=L[0]
    min_cnt=N
    dfs(0,1)
    print(f"#{tc} {min_cnt}")

    