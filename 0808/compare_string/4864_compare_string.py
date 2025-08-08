import sys
sys.stdin = open('4864_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = 0
    for i in range(len(str2)-len(str1)+1):
        check_str2 = str2[i:i+len(str1)]
        if str1 == check_str2:
            result = 1

    print(f'#{tc} {result}')