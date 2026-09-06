# 8방향 탐색용 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    # 지형 높이 정보 입력받기
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        
    candidate_cnt = 0 # 예비 후보지 개수
    
    # 모든 위치를 하나씩 착륙지로 지정해서 확인
    for r in range(N):
        for c in range(M):
            lower_cnt = 0 # 현재 위치보다 낮은 주변 구역 수
            
            # 8방향 탐색
            for i in range(8):
                nr = r + dx[i]
                nc = c + dy[i]
                
                # 영역 벗어나지 않는지 확인
                if 0 <= nr < N and 0 <= nc < M:
                    # 주변 높이가 착륙지 높이보다 낮으면 카운트
                    if grid[nr][nc] < grid[r][c]:
                        lower_cnt += 1
            
            # 낮은 곳이 4곳 이상이면 후보지로 인정
            if lower_cnt >= 4:
                candidate_cnt += 1
                
    print(f"#{tc} {candidate_cnt}")