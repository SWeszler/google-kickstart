
def solution(N, days):
    count = 0
    for i, d in enumerate(days):
        if (i == 0 or d > days[i - 1]) and (i == N - 1 or d > days[i + 1]):
            count += 1
        if i > 0:
            days[i] = max(d, days[i - 1])

    return count


tc = int(input())
for i in range(1, tc + 1):
    N = input()
    days = [int(p) for p in input().split()]
    out = solution(int(N), days)
    print("Case #{}: {}".format(i, out))