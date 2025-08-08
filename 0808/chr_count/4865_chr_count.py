import sys
sys.stdin = open('4865_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    new_str1 = []   # 중복되지 않게 문자들을 하나씩 추가
    for i in str1:
        if i not in new_str1:
            new_str1.append(i)

    max_count = 0
    for i in new_str1:
        count = 0
        for j in str2:
            if i == j:  # i와 같은 문자들이 보일 때 마다 count를 증가
                count += 1
        if max_count < count:
            max_count = count

    print(f'#{tc} {max_count}')
