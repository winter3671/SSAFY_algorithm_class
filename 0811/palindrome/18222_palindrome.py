import sys
sys.stdin = open('4861_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = None

    for i in range(N):  # 가로를 검증
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+(M-1)-k]:
                    break
            else:
                result = arr[i][j:j+M]  # arr[i][j]부터 M만큼을 슬라이싱으로 반환
                break

    for j in range(N):  # 세로를 검증
        for i in range(N-M+1):
            for k in range(M//2):
                if arr[i+k][j] != arr[i+(M-1)-k][j]:
                    break
            else:
                list_result = list(arr[i+l][j] for l in range(M))   # 각 arr의 요소의 j번째를 모아 .join()으로 합침
                result = ''.join(list_result)
                break

    print(f'#{tc} {result}')