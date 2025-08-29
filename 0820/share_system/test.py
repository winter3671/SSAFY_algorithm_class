target1 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
check_nums1 = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1]

N = 10
cnt = 0
i = 0

while check_nums1 != target1:  # 두 리스트가 완전히 일치할때까지 반복
    while i < 10:
        if check_nums1[i] != target1[i]:
            for j in range(N):
                if check_nums1[j] == target1[i]:
                    check_nums1[j], check_nums1[j - 1] = check_nums1[j - 1], check_nums1[j]
                    cnt += 1
                    break
        else:
            i += 1
print(cnt)