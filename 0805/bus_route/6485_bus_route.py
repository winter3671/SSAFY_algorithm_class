import sys

sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    bus_list = [0] * 5000

    N = int(input())
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for num in range(Bi - Ai + 1):   # Ai와 Bi의 차이만큼 인덱스에 맞는 bus_list에 1을 각각 더함
            bus_list[Ai-1+num] += 1

    P = int(input())
    result_list = []
    for j in range(P):
        Cj = int(input())
        result_list.append(bus_list[Cj-1])

    print(f'#{tc} {" ".join(map(str, result_list))}')   # str형으로 바꾼 뒤 .join() 사용