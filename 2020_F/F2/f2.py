import sys

def solution_bf(N, K, intervals):
    intervals.sort()
    count = 0
    harvest = 0

    for S, E in intervals:
        if S > harvest:
            harvest = S + K
            count += 1

        while E > harvest:
            count += 1
            harvest += K
    
    return count

def solution_fast(N, K, intervals):
    intervals.sort()
    count = 0
    harvest = 0

    for S, E in intervals:
        if S > harvest:
            harvest = S + K
            count += 1

        if E > harvest:
            m = -(-(E - harvest) // K)
            count += m
            harvest += m * K
    
    return count

solution = solution_fast

tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    intervals = []
    for n in range(int(N)):
        S, E = input().split()
        intervals.append((int(S), int(E)))

    out = solution(int(N), int(K), intervals)
    print("Case #{}: {}".format(i, out))