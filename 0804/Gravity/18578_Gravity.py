import sys

# 현재 파일과 같은 위치에 있는 sample_input.txt 파일을 열어서 input 으로 가져가겠다.
sys.stdin = open('input.txt')
# input() 호출 시 'sample_input.txt'의 한 줄 씩 읽어서 가져옴
# input 함수는 return 값이 문자열임!

# 테스트 케이스 개수 설정
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))

    fall_list = []
    for i in range(N): # 각 줄의 상자들에 대해
        count = 0
        for j in range(i+1, N): # 지정 줄의 상자 아래의 줄들에 대해서
            if box_list[i] <= box_list[j]:  # 지정 줄의 상자의 길이보다 크거나 같은 줄이 있다면
                count += 1
        fall_list.append((N-i-1)-count)

    max_fall = 0
    for num in fall_list:
        if max_fall < num:
            max_fall = num

    print(f'#{tc} {max_fall}')