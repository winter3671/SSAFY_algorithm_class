import sys

# 현재 파이썬 파일과 같은 위치에 있는 input.txt 파일을 열어서 input으로 넣겠다.
# sys.stdin = open('input.txt')
# input() 호출시 'input.txt'의 한 줄씩 읽어서 가져옴
# input 함수는 리턴값이 문자열!!!

# 테스트 케이스 개수 설정
# T = 10
# for tc in range(1, T+1):
# N = int(input())   # 덤프 횟수
# box_list = list(map(int, input().split())) # 상자의 높이값
N = 1
box_list = [99, 99, 999]
max_idx = 0
min_idx = 0
max_box = 0
min_box = 0
for _ in range(N):
    # box_list의 max, min 구함. 100 1
    for i in range(len(box_list)):
        if box_list[max_idx] < box_list[i]:
            max_idx = i
        if box_list[min_idx] > box_list[i]:
            min_idx = i
    # 덤프 실행
    box_list[max_idx] -= 1
    box_list[min_idx] += 1

    for i in range(len(box_list)):
        if box_list[max_idx] < box_list[i]:
            max_idx = i
        if box_list[min_idx] > box_list[i]:
            min_idx = i

    # 평탄화 확인
    if box_list[max_idx] - box_list[min_idx] <= 1:
        break
gap = box_list[max_idx] - box_list[min_idx]
print(f"# {gap}")
