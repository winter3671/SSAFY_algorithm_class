import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    nums = []
    for i in range(N):  # nums에 숫자가 들어가는 공간만큼 [0]을 생성
        nums.append([0] * (i+1))

    nums[0][0] = 1    # 맨 처음 숫자는 1

    for i in range(1, N):   # 각 줄의 맨앞과 맨 뒤는 1로 고정
        nums[i][0] = 1
        nums[i][i] = 1

        if i >= 2:      # 세번째 줄의 1을 제외한 나머지 수는 규칙을 따라 생성
            for j in range(1, i):
                nums[i][j] = nums[i-1][j-1] + nums[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(nums[i][j], end = ' ')
        print()