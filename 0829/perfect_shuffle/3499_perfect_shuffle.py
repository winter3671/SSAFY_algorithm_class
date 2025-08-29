import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = list(input().split())

    if N % 2 == 1:
        s