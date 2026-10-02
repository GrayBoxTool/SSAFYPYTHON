import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(product, cost):
    global min_cost

    # 가지치기
    if cost >= min_cost:
        return

    # 모든 제품 배정 완료
    if product == N:
        min_cost = cost
        return

    # 현재 제품을 생산할 공장들을
    # 기회비용이 작은 순서대로 탐색
    factories = []

    for factory in range(N):
        if visited[factory] == 0:
            factories.append(factory)

    factories.sort(key=lambda factory: tmp[factory][product])

    for factory in factories:
        visited[factory] = 1

        dfs(
            product + 1,
            cost + L[factory][product]
        )

        visited[factory] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    # tmp[공장][제품] = 해당 공장에서 그 제품을 생산할 기회비용
    tmp = [[0] * N for _ in range(N)]

    for factory in range(N):
        cost_sum = sum(L[factory])

        for product in range(N):
            tmp[factory][product] = (
                L[factory][product]
                / (cost_sum - L[factory][product])
            )

    visited = [0] * N
    min_cost = N * 100

    dfs(0, 0)

    print(f"#{tc} {min_cost}")