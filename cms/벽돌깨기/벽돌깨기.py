import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N,W,H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    