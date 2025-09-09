import sys
sys.stdin = open('sample_input.txt')

def combinations(num_list, lev, start, lst, num):       # 부분집합을 만드는 함수,
    if lev == num:
        lst.append(q[:])
        return

    for i in range(start, len(num_list)):
        q.append(num_list[i])
        combinations(num_list, lev+1, i+1, lst, num)
        q.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    q = []

    ing_lst = []
    ing_lst_1 = []
    ing_lst_2 = []

    N_num = [i for i in range(1, N+1)]
    combinations(N_num, 0, 0, ing_lst, N//2)    # N//2개의 원소를 가진 집합들을 N-num에 저장

    for i in range(len(ing_lst)//2):    # ing_lst_1과 ing_lst_2에 순서대로, 정 반대의 재료가 들어가도록 투입
        ing_lst_1.append(ing_lst[i])    # N = 6이고, ing_lst_1[i]가 [1, 2, 5]라면
        ing_lst_2.append(ing_lst[len(ing_lst) - i - 1])     # ing_lst_2[i]는 [3, 4, 6]이 들어가도록 함

    min_result = float('inf')
    for i in range(len(ing_lst_1)):
        case1 = []
        case2 = []
        combinations(ing_lst_1[i], 0, 0, case1, 2)      # ing_lst_1에 있는 재료들 중 2개의 원소를 가진 부분집합들을 저장
        combinations(ing_lst_2[i], 0, 0, case2, 2)
        sum_taste_1 = 0
        sum_taste_2 = 0
        for x, y in case1:      # 예를 들어,  x = 1, y = 2일 때
            sum_taste_1 += arr[x-1][y-1]       # arr[1][2]가 들어가면
            sum_taste_1 += arr[y-1][x-1]       # arr[2][1]도 계산해서 같이 더해줌
        for x, y in case2:
            sum_taste_2 += arr[x-1][y-1]
            sum_taste_2 += arr[y-1][x-1]
        result = abs(sum_taste_1 - sum_taste_2)     # 두 맛의 차이
        if min_result > result:
            min_result = result

    print(f'#{tc} {min_result}')
