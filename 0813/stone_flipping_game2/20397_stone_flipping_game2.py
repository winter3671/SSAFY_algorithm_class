import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

