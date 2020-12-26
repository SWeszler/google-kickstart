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


solution = solution_bf

tc = int(raw_input())
for i in xrange(1, tc + 1):
    N, K = raw_input().split()
    intervals = []
    for n in xrange(int(N)):
        S, E = raw_input().split()
        intervals.append((int(S), int(E)))

    out = solution(int(N), int(K), intervals)
    print("Case #{}: {}".format(i, out))