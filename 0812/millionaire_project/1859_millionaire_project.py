import sys
sys.stdin = open('input.txt')

# def max_sale(nums, sum_cnt):
#     max_cnt = 0     # nums의 최댓값
#     for i in range(len(nums)):
#         if max_cnt < nums[i]:
#             max_cnt = nums[i]
#     if nums == []:      # nums가 빈 리스트일때(맨 마지막이 최댓값으로 끝날 때)
#         return sum_cnt
#
#     for i in range(nums.index(max_cnt)):    # 구간의 최댓값의 index만큼 반복
#         sum_cnt += max_cnt - nums[i]    # 최댓값과 각 가격의 차를 sum_cnt에 더해줌
#
#     new_nums = nums[nums.index(max_cnt)+1:]     # 최댓값 다음 구간부터 끝까지를 새로운 nums로 정하고, 재귀
#     return max_sale(new_nums, sum_cnt)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#
#     result = max_sale(nums, 0)
#     print(f'#{tc} {result}')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    sum_num = 0
    max_num = 0
    for i in range(N-1, -1, -1):    # N의 역순으로 순회하며
        if max_num <= nums[i]:  # 최댓값보다 nums[i]가 더 크다면
            max_num = nums[i]   # 최댓값을 교체
        else:
            sum_num += max_num - nums[i]    # 최댓값보다 더 작으면, 그 차만큼 sum_num에 합함

    print(f'#{tc} {sum_num}')

