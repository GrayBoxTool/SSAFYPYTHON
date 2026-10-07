# MST(Prim, Kruskal)
# 최단경로(Dijkstra)

# Prim : MST를 만들어가는 알고리즘

# 1. 임의의 정점 선택
# 2. 선택한 정점들에 연결되는 간선중에 최소비용 
#   간선선택
# 3. 최소 비용 간선을 선택하면 하나의 새로운 정점이 선택됨
# 4. kruskal : MST를 만드는 알고리즘

# 무향 그래프
# 6 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51


def prim(start):
    # MST에 선택된 정점들로 부터 각 정점들로 가는 비용
    weights=[0xffffffff]*(V+1)
    MST=set([start])
    weights[start]=0

    # 선택된 정점들에서 다른 정점으로 가는 비용중에 최소비용 선택하기
    while True:
        if len(MST)==V+1:
            break
        # 다른 정점으로 가는 비용중에 최소비용 선택하기
        min_idx = -1
        min_v = 0xffffffff

        for i in range(V+1):    # i : 정점번호
            if i not in MST and weights[i]<min_v:
                min_idx=i
                min_v=weights[i]
        # 최소 비용으로 갈 수 있는 정점이 선택
        MST.add(min_idx)

        for i in range(V+1):
            # 원래 내가 알고 있던 i번 연결비용 : weights[i]
            # min_idx가 추가되면서 새로운 연결비용 : adj[min_idx][i]
            if adj[min_idx][i] and i not in MST and adj[min_idx][i]<weights[i]:
                weights[i] = adj[min_idx][i]

    print(weights)


V,E=map(int,input().split())
# 인접행렬
adj=[[0]*(V+1)for _ in range(V+1)]
for _ in range(E):
    a,b,w=map(int,input().split())
    adj[a][b]=w
    adj[b][a]=w

for row in adj:
    print(row)

prim(0)

