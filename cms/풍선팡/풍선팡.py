import sys
sys.stdin = open("input1.txt", "r")

# 케이스 갯수 할당
T = int(input())
for test_case in range(1, T + 1):
    row, col = map(int, input().split())
    board = []
    for i in range(row):
        board.append(list(map(int,input().split())))
    result = 0
    for i in range(row):
        for j in range(col):
            count = 0
            num = board[i][j]
            count += num
            for k in range(1, num+1):
                if i-k >= 0 :
                    count += board[i-k][j]
                if i+k <= len(board)-1:
                    count += board[i+k][j]
                if j-k >= 0 :
                    count += board[i][j-k]
                if j+k <= len(board[i])-1:
                    count += board[i][j+k]
            if count > result :
                result = count
    print(f"#{test_case} {result}")