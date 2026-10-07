# # DFS (인접 리스트)= 가능한 모든 정점 1번씩 탐색
# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3

name = "BACD"
n,m=map(int,input().split())    # 정점,간선 정보의 개수
arr= [[]for _ in range(n)]
for _ in range(m):
    start,end=map(int,input().split())
    arr[start].append(end)

used=[0]*n
cnt=0

def dfs(now):
    global cnt
    if now==3:   # if name[now]=='D'
        cnt+=1

    for i in arr[now]:
        if used[i]==0:
            used[i]=1
            dfs(i)
            used[i]=0

used[1]=1
dfs(1)
print(cnt)