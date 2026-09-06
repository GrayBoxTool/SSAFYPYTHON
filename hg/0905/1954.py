# import sys
# sys.stdin = open("input.txt", "r")

# 오른쪽, 아래, 왼쪽, 위 (시계방향 순서)
# (y변화량, x변화량)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    # NxN 크기 0으로 초기화된 배열 만들기
    board = [[0] * N for _ in range(N)]
    
    # 현재 위치와 direction(방향) 변수
    y = 0
    x = 0
    dir_idx = 0  # 0:오른쪽, 1:아래, 2:왼쪽, 3:위
    
    # 1부터 N*N까지 채우기
    for num in range(1, N * N + 1):
        board[y][x] = num
        
        # 다음 이동할 위치 미리 계산해보았음
        ny = y + dy[dir_idx]
        nx = x + dx[dir_idx]
        
        # 범위를 벗어나거나, 이미 숫자가 채워진 칸(0이 아닌 칸)을 만난 경우
        if ny < 0 or ny >= N or nx < 0 or nx >= N or board[ny][nx] != 0:
            # 방향 바꾸기 (오른쪽 -> 아래 -> 왼쪽 -> 위 -> 오른쪽...)
            dir_idx = (dir_idx + 1) % 4
            ny = y + dy[dir_idx]
            nx = x + dx[dir_idx]
            
        # 실제 위치 이동
        y = ny
        x = nx

    # 결과 출력
    print(f"#{test_case}")
    for row in board:
        print(*row)