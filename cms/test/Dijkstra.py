# 1. 시작점에서 다른 정점까지 가는 비용계산
# 2. 그 중에서 가장 작은 비용이면 경로 확정
# 3. 그 경로로 다른 정점까지 가능 비용 계산해보고, 더 작으면 수정..
# 4. 목적지 까지 비용이 확정될 때 까지 1~3 반복

# 5 11
# 0 1 3
# 0 2 5
# 1 2 2
# 1 3 6
# 2 1 1
# 2 3 4
# 2 4 6
# 3 4 2
# 3 5 3
# 4 0 3
# 4 5 6

V,E=map(int,input().split())
adj=[[0]*(V+1)for _ in range(V+1)]
for _ in range(E):
    s,e,w=map(int, input().split())
    adj[s][e]=w

def dijkstra(start,end):
    # weights: 시작점에서 다른 정점으로 가는 비용
    weights=[0xfffffff]*(V+1)
    # 이미 비용계산이 완료되었는지 여부 체크
    done=[0]*(V+1)
    weights[start]=0

    while True:
        # 시작점에서 최소비용으로 갈 수 있는 정점 찾기
        min_idx=-1
        min_v=0xfffffff
        for i in range(V+1):
            if not done[i] and weights[i]<min_v:
                min_idx=i
                min_v=weights[i]
                done[min_idx]=1 #해당 정점까지 가는 비용 확정
        if min_idx==end:    #목적지 까지 비용 계산했으면 멈춤
            break

        # 한 정점까지 가는 비용이 확정, 그 정점을 경유해서 다른 정점으로 가는 비용계산
        # 만약 정점을 경유해서 다른 정점까지 가는 비용이 더 작으면 비용 수정
        # 새롭게 선택된 정점(min_idx)에서 다른 정점들 까지 비용 계산: adj[min_idx][i]
        for i in range(V+1):
            # 연결되어 있고, 시작점에서 min_idx까지 비용+ adj[min_idx][i]
            # weights[min_idx]+adj[min_idx][i]
            # 원래 알고 있던 시작점에서 i 까지 가는 비용
            # weights[i]

            if adj[min_idx][i] and not done[i] and (weights[min_idx]+adj[min_idx][i])<weights[i]:
                weights[i] = weights[min_idx]+adj[min_idx][i]

    return weights

print(dijkstra(0,5))



