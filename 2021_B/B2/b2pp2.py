def solution_bf(N, A):
    if N <= 2:
        return 2

    res = 0
    for i in range(1, N):
        diff = A[i] - A[i - 1]
        A1 = A[:]
        count = 1
        fix = 1
        for j in range(i, N):
            if diff == A1[j] - A1[j - 1]:
                count += 1
            elif fix <= 0:
                break
            else:
                count += 1
                fix -= 1
                A1[j] = A1[j - 1] + diff
        
        count += fix
        count = N if count > N else count
        res = max(count, res)

        if i < N - 2:
            diff = (A[i + 1] - A[i - 1]) // 2
            A1 = A[:]
            count = 1
            fix = 1
            for j in range(i, N):
                if diff == A1[j] - A1[j - 1]:
                    count += 1
                elif fix <= 0:
                    break
                else:
                    count += 1
                    fix -= 1
                    A1[j] = A1[j - 1] + diff
            
            res = max(res, count)

    return res


solution = solution_bf


tc = int(input())
for i in range(1, tc + 1):
    N = input()
    A = [int(a) for a in raw_input().split()]
    out = solution(int(N), A)
    print("Case #{}: {}".format(i, out))