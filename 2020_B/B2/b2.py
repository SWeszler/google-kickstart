
def solution_slow1(N, D, buses):
    res = D
    i = len(buses) - 1

    while i >= 0:
        for j in range(min(res, D), 0, -1):
            if j % buses[i] == 0:
                res = min(res, j)
                i -= 1
                break
    return res

def solution_slow2(N, D, buses):
    res = None
    new_row = [1] + [0 for x in range(N)]
    dp = [new_row]

    for i in range(D):
        
        for j in range(1, N + 1):
            if ((D - i) % buses[N - j] == 0 or dp[i - 1][j]) and dp[i][j - 1]:
                dp[i][j] = 1

        if all(dp[i]):
            res = D - i
            break

        dp.append(new_row)
            
    return res

def solution_slow3(N, D, buses):
    res = None
    left = 0
    right = D

    def helper(start):
        states = [1]+[0 for i in range(N)]
        for i in range(start, D + 1):
            for j in range(1, N + 1):
                if i % buses[j - 1] == 0 and states[j - 1]:
                    states[j] = 1
            if all(states):
                return True

    while left <= right:
        mid = (left + right) // 2
        if helper(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return res

def solution(N, D, buses):
    res = None
    left = 0
    right = D

    def helper(start):
        from math import ceil
        for j in range(N):
            first_day = ceil(start/buses[j])*buses[j]
            if not (start <= first_day <= D):
                return False
            start = first_day
        return True

    while left <= right:
        mid = (left + right) // 2
        if helper(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return res
    


tc = int(input())
for i in range(1, tc + 1):
    N, D = input().split()
    input_list = [int(p) for p in input().split()]
    out = solution(int(N), int(D), input_list)
    print("Case #{}: {}".format(i, out))