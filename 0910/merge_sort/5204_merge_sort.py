import sys
sys.stdin = open('5204_input.txt')

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:    # 정렬 전에, left의 가장 오른쪽 원소와 right의 가장 오른쪽 원소 크기 비교
        cnt += 1

    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1


    return result

def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merge_list = merge(left_list, right_list)
    return merge_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    merge_list = merge_sort(nums)

    print(f'#{tc} {merge_list[N//2]} {cnt}')
