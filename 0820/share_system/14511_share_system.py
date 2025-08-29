import sys
sys.stdin = open('Sample_input.txt')

def check_target(nums_list, my_target):
    global cnt
    while nums_list != my_target:   # 두 리스트가 완전히 일치할때까지 반복
        i = 0
        while i < 10:
            if nums_list[i] != my_target[i]:
                for j in range(N):
                    if nums_list[j] == my_target[i]:
                        nums_list[j], nums_list[j - 1] = nums_list[j - 1], nums_list[j]
                        cnt += 1
                        break
            else:
                i += 1
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    odd_count = 0
    even_count = 0
    cnt = 0

    for i in range(N):      # 모든 홀수는 1으로, 모든 짝수는 0으로 변환
        if nums[i] % 2 == 0:
            nums[i] = 0
            even_count += 1
        else:
            nums[i] = 1
            odd_count += 1

    if even_count - odd_count == 1:     # 짝수가 홀수보다 1개 많을때
        target = [0, 1] * (N // 2) + [0]
        check_target(nums, target)

    elif odd_count - even_count == 1:     # 홀수가 짝수보다 1개 많을때
        target = [1, 0] * (N // 2) + [1]
        check_target(nums, target)

    elif even_count - odd_count == 0:      # 짝수와 홀수의 갯수가 같을 때,
        target1 = [0, 1] * (N // 2)
        check_nums1 = nums[:]
        check_target(check_nums1, target1)
        first_cnt = cnt

        cnt = 0
        target2 = [1, 0] * (N // 2)
        check_nums2 = nums[:]
        check_target(check_nums2, target2)
        second_cnt = cnt

        if first_cnt <= second_cnt:
            cnt = first_cnt
        else:
            cnt = second_cnt

    else:       # 불가능
        cnt = -1

    print(cnt)
    '''
    11101000
    11011000
    10111000
    10110100
    10101100
    10101010
    
    11011000
    10111000
    01111000
    01110100
    01101100
    01011100
    01011010
    01010110
    01010101
    '''