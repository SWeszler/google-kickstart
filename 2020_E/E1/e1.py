def solution(arr, N):
    m = 0
    diffs = [0]
    for i in range(1, N):
        diffs.append(arr[i - 1] - arr[i])

    count = 1
    for i in range(1, N):
        if diffs[i - 1] == diffs[i]:
            count += 1
        else:
            count = 2
        m = max(m, count)
    return m


tc = int(input())
for i in range(1, tc + 1):
    N = input()
    arr = [int(p) for p in input().split()]
    out = solution(arr, int(N))
    print("Case #{}: {}".format(i, out))