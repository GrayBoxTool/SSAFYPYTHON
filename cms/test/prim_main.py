import heapq

n=int(input())  #노드의 수
m=int(input())  #간선의 수

arr=[[]for _ in range(n)]

# 무방향 그래프이므로 양방향 저장
for _ in range(m):
    start, end, cost = map(int, input().split())

    arr[start].append((cost,end))
    arr[end].append((cost,start))

used=[0]*n  #내가 선택한 정점인지 체크
heap=[] #최소비용을 뽑기위함

# (비용, 정점)
heapq.heappush(heap,(0,0))  #비용 시작 정점

total=0 #총 비용을 합치기
cnt=0   #연결한 정점의 개수

while heap:
    cost, now = heapq.heapppop(heap)

    # 이미 MST에 포함된 정점이면 무시
    if used[now]==1:
        continue

    # MST에 정점 포함
    used[now]=1 #방문체크
    total+=cost #비용의 합
    cnt+=1      #연결된 간선의 개수 1증가

    # 모든 정점을 선택 했다면 종료
    if cnt == n:
        break

    # 현재 정점과 연결된 간선들을 우선순위 큐에 추가
    for next_cost, next_node in arr[now]:
        if used[next_node]==0:
            heapq.heappush(heap, (next_cost,next_node))
print(total)