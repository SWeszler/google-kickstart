def solution(R, C, m):
    pass

tc = int(input())
for i in range(1, tc + 1):
    R, C = input().split()
    m = []
    for j in range(int(R)):
        m.append([int(c) for c in input().split()])
    out = solution(int(R), int(C), m)
    print("Case #{}: {}".format(i, out))