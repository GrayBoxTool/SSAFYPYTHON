import sys
from collections import deque

sys.stdin=open("sample_input.txt","r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(N)]

    q = deque()

    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 'W':
                q.append(r * M + c)

    result = 0
    distance = 0

    while q:
        size = len(q)
        for _ in range(size):
            pos = q.popleft()
            r, c = divmod(pos, M)

            nr = r - 1
            if nr >= 0 and matrix[nr][c] == 'L':
                matrix[nr][c] = 'W'
                q.append(nr * M + c)
                result += distance + 1

            nr = r + 1
            if nr < N and matrix[nr][c] == 'L':
                matrix[nr][c] = 'W'
                q.append(nr * M + c)
                result += distance + 1

            nc = c - 1
            if nc >= 0 and matrix[r][nc] == 'L':
                matrix[r][nc] = 'W'
                q.append(r * M + nc)
                result += distance + 1

            nc = c + 1
            if nc < M and matrix[r][nc] == 'L':
                matrix[r][nc] = 'W'
                q.append(r * M + nc)
                result += distance + 1

        distance += 1

    print(f"#{tc} {result}")