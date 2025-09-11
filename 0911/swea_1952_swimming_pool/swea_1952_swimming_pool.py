import sys
sys.stdin = open('sample_input.txt')

def search_qurter(cost, start):
    global sum_cost
    if

    for i in range(start+1, 14):
        if visited[i] == 0:
            q.append(i)
            visited[i], visited[i+1], visited[i+2] = 1, 1, 1
            search_qurter(cost, i+2)



T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    month_plan = list(map(int, input().split()))

    month_price = [0] * 12
    sum_cost = 0

    for i in range(12):
        month_price[i] = min(day * month_plan[i], month)
        sum_cost += month_price[i]

    q = 0
    visited = [0] * 16
    max_cost = 0

    print(month_price)


    # 1일 vs 1달 중 선택
    # 1일치 가격 * 월 이용 숫자 vs 1달치 가격

    # 1달 vs 3달 중 선택
    # 1달 * 1 > 3달
    # 1달 * 2 > 3달 > 1달 * 1
    # 1달 * 3 > 3달 > 1달 * 2
