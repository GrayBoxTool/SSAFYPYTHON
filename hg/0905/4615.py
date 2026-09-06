#누구에게 재밌는 오셀로 게임인가 진짜 오셀로 재미없고하기실ㅎ다

# 8방향 탐색용 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    # N x N 크기의 보드 만들기 (0으로 초기화)
    board = [[0] * N for _ in range(N)]
    
    # 정중앙 초기 돌 배치
    mid = N // 2
    board[mid - 1][mid - 1] = 2  # W
    board[mid - 1][mid] = 1      # B
    board[mid][mid - 1] = 1      # B
    board[mid][mid] = 2          # W

    for _ in range(M):
        # 1-based 인덱스를 0-based 인덱스로 변환
        col, row, color = map(int, input().split())
        x, y = row - 1, col - 1
        
        # 돌을 놓음
        board[x][y] = color
        
        # 8방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 뒤집을 돌들의 위치를 담을 리스트
            to_flip = []
            
            # 보드 범위 안이고, 상대방 돌이 있는 동안 계속 이동
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0 and board[nx][ny] != color:
                to_flip.append((nx, ny))
                nx += dx[i]
                ny += dy[i]
            
            # 상대방 돌 뒤에 내 돌이 있다면 리스트에 담긴 돌들을 모두 내 색으로 바꿈
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                for fx, fy in to_flip:
                    board[fx][fy] = color

    # 최종 흑돌(1), 백돌(2) 개수 세기
    black_cnt = 0
    white_cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                black_cnt += 1
            elif board[r][c] == 2:
                white_cnt += 1

    print(f"#{tc} {black_cnt} {white_cnt}")