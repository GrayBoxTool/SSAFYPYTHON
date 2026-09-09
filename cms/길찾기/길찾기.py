import sys
sys.stdin = open("input.txt","r")

def dfs(maze):
    N=len(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] ==2:
                sr=i
                sc=j
    stack=[]
    stack.append((sr,sc))
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1

    while stack:
        cr,cc = stack[-1]
        if maze[cr][cc] ==3 :
            return 1
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = cr+dr
            nc = cc+dc
            if 0<=nr<N and 0<=nc <N and maze[nr][nc] != 0 and visited[nr][nc]==0:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else :
            stack.pop()
    return 0

for _ in range(1,11):
    tc, N = map(int, input().split())
    maze = list(map(int,input().split()))
    print(f"{tc} {dfs(maze)}")