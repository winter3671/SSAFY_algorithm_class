import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0

    for i in range(8):  # 가로로 검사
        for j in range(8-N+1):  # 회문검사 시작점의 최대범위
            for k in range(N//2):   # N의 절반만 검사하면 됨
                if arr[i][j+k] != arr[i][j+(N-1)-k]:    # 두 대칭점이 일치하지 않으면 break
                    break
            else:   # break에 걸리지 않는다면 cnt를 1 증가
                cnt += 1

    for j in range(8):  # 세로로 검사
        for i in range(8-N+1):
            for k in range(N//2):
                    if arr[i+k][j] != arr[i+(N-1)-k][j]:
                        break
            else:
                cnt += 1

    print(f'#{tc} {cnt}')