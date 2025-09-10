import sys
sys.stdin = open('input.txt')

def quick_sort(left, right):
    pivot = nums[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and nums[i] <= pivot:      # i번째 수가 pivot 보다 작거나 같으면
            i += 1

        while i <= j and nums[j] >= pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[j], nums[left] = nums[left], nums[j]

    if right - left <= 1:
        return

    if j > left:
        quick_sort(left, j-1)
    if j < right:
        quick_sort(j+1, right)



T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    quick_sort(0, len(nums)-1)

    print(f'#{tc} {" ".join(map(str, nums))}')