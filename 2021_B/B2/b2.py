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


def solution_optimal(N, A):
    import collections
    D = []
    res = 0
    chunks = collections.defaultdict(list)

    for i in range(1, N):
        D.append(A[i] - A[i -1])

    d = D[0]
    k = 0
    len_D = len(D)
    for i in range(len_D):
        if D[i] == d:
            chunks[k].append(D[i])
        else:
            d = D[i]
            k = i
            chunks[k].append(D[i])


    for i, chunk in chunks.items():
        k = len(chunk)
        l = k + 1
        if i + k + 1 == len_D:
            l += 1
        elif i + k + 1 < len_D and D[i + k] + D[i + k + 1] == 2 * chunk[0]:
            l += 2
        if i + k + 2 < len_D - 1 and D[i + k] + D[i + k + 1] == 2 * chunk[0] and D[i + k + 2] == chunk[0]:
            l += len(chunks[i + k + 2])
        res = max(res, l)

    chunks = collections.defaultdict(list)
    d = D[-1]
    k = len_D - 1
    len_D = len(D)
    for i in range(len_D - 1, -1, -1):
        if D[i] == d:
            chunks[k].append(D[i])
        else:
            d = D[i]
            k = i
            chunks[k].append(D[i])

    for i, chunk in chunks.items():
        k = len(chunk)
        l = k + 1
        if i - k - 1 == 0:
            l += 1
        elif i - k - 1 >= 0 and D[i - k] + D[i - k - 1] == 2 * chunk[0]:
            l += 2
        if i - k - 2 >= 0 and D[i - k] + D[i - k - 1] == 2 * chunk[0] and D[i - k - 2] == chunk[0]:
            l += len(chunks[i - k - 2])
        # print('i:', i, chunk, l)

        res = max(res, l)

    return res


solution = solution_optimal


tc = int(input())
for i in range(1, tc + 1):
    N = input()
    A = [int(a) for a in input().split()]
    # if i != 5:
    #     continue
    out = solution(int(N), A)
    print("Case #{}: {}".format(i, out))