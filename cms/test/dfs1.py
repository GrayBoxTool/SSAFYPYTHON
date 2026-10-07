# DFS (인접 행렬) = 가능한 모든 정점 1번씩 탐색
name="BACD"
arr =[
    [0,0,1,1],
    [1,0,1,0],
    [1,0,0,1],
    [0,0,0,0]]

used=[0]*4 # 정점의 개수만큼 방문체크

def dfs(now):
    print(name[now], end=" ")
    for i in range(4):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1
            dfs(i)

used[1]=1 # 탐색 시작 인덱스에 1 중복체크
dfs(1)  # 탐색 시작 인덱스