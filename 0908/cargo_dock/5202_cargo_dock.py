import sys
sys.stdin = open('5202_input.txt')

def find_cargo():
    global cnt
    current_end = 0
    end_idx = 0
    check = True
    while current_end < 24 and check is True:   # current_end가 24가 되거나, 더이상 가능한 화물차가 없으면 종료
        check = False
        for idx in range(end_idx, N):   # end_idx부터 탐색
            if arr[idx][0] >= current_end:      # 이전 화물차의 완료 시간보다 시작시간이 더 늦은 차 중에서
                current_end = arr[idx][1]       # 가장 앞의 화물차를 지정, 화물차의 완료 시간을 저장
                cnt += 1
                end_idx = idx+1     # end_idx는 탐색한 idx 다음 화물차
                check = True    # check가 True가 아니라면 더이상 가능한 화물차가 없는 것
                break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    arr.sort(key = lambda x:x[1])    # x[1]을 기준으로 오름차순 정렬
    cnt = 0

    find_cargo()

    print(f'#{tc} {cnt}')