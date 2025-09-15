import sys
sys.stdin = open('sample_input.txt')

def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = []
    for i in range(0, 2*M, 2):
        x, y = nums[i], nums[i+1]
        arr.append([x, y])

    parents = make_set(N)
    for sets in arr:
        union(sets[0], sets[1])

    set_group = set(find_set(i) for i in range(1, N+1))

    print(f'#{tc} {len(set_group)}')