import sys

# 현재 파일과 같은 위치에 있는 sample_input.txt 파일을 열어서 input 으로 가져가겠다.
sys.stdin = open('sample_input.txt')
# input() 호출 시 'sample_input.txt'의 한 줄 씩 읽어서 가져옴
# input 함수는 return 값이 문자열임!

# 테스트 케이스 개수 설정
T = 10
for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int, input().split()))

    view = 0    # 조망권이 확보된 세대의 수
    for i in range(2, N-2):
        highest_building = 0
        buildings = [building_list[i-2], building_list[i-1], building_list[i+1], building_list[i+2]]    # 주변 4대의 빌딩
        for j in buildings:
            if highest_building < j:
                highest_building = j    # 주변 4대의 빌딩의 최대높이
        if highest_building < building_list[i]: # 이 빌딩이 주변 4대보다 높다면,
            view += building_list[i] - highest_building
            # 빌딩의 높이에서 주변 4대의 빌딩의 높이의 최댓값을 뺀 값을 view에 추가

    print(f'#{tc} {view}')

