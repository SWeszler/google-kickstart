def solution_bf(L, R):
    count = 0

    for n in range(L, R + 1):
        i = 1
        found = True
        for d in str(n):
            if (int(d) % 2 == 0 and i % 2 != 0) or (int(d) % 2 != 0 and i % 2 == 0):
                found = False
                break
            i += 1

        if found:
            count += 1

    return count


def solution_faster(L, R):
    count = 0
    l = [int(d) for d in str(L)]

    def is_even(N):
        return not N % 2

    i = len(l) - 1
    while i >= 0:
        if is_even(i + 1) != is_even(l[i]):
            l[i] += 1
            l[i - 1] += l[i] // 10
            l[i] = l[i] % 10
            l = l[:i + 1] + [0] * (len(l) - 1 - i)
            i = len(l) - 1
        else:
            l[i - 1] += l[i] // 10
            l[i] = l[i] % 10
            i -= 1

        if l[0] >= 10:
            l[0] = l[i] % 10
            l = [l[i] // 10] + l
            i += 1

    L = int(''.join([str(d) for d in l]))


    while L <= R:
        a = [int(d) for d in str(L)]
        i = len(a) - 1
        a[i] += 2
        c = a[i]

        while c >= 10:
            a[i] = c % 10
            i -= 1

            if i < 0:
                a = [0 if is_even(i + 1) else 1 for i in range(len(a) + 1)]
                break

            a[i] += 1
            if is_even(i + 1) != is_even(a[i]):
                a[i] += 1

            c = a[i]
        
        count += 1
        L = int(''.join([str(d) for d in a]))

    return count


def solution_fastest(L, R):
    intervals = []
    l = 1
    last = 0
    rsum = 0
    lsum = 0
    
    while 10**l - 10**(l-1) < R - last:
        intervals.append([last + 1, last + 10**l - 10**(l-1), l])
        last += 10**l - 10**(l-1)
        l += 1

    while last < R:
        if R - last < 10:
            intervals.append([last + 1, R, 0])
            break
        elif 10**(l-1) < R - last:
            intervals.append([last + 1, last + 10**(l-1), l-1])
            last += 10**(l-1)
        else:
            l -= 1

    for s, e, l in intervals:
        if l != 0:
            e = s
        for n in range(s, e + 1):
            i = 1
            boring = True
            for d in str(n):
                if i % 2 != int(d) % 2:
                    boring = False
                i += 1
                if i > len(str(n)) - l:
                    break
            if boring and l == 0:
                rsum += 1

        if boring and l != 0:
            rsum += 5**l

    l = 1
    last = 0
    intervals = []
    while 10**l - 10**(l-1) < L - last:
        intervals.append([last + 1, last + 10**l - 10**(l-1), l])
        last += 10**l - 10**(l-1)
        l += 1

    while last < L - 1:
        if L - last < 10:
            intervals.append([last + 1, L - 1, 0])
            break
        elif 10**(l-1) < L - 1 - last:
            intervals.append([last + 1, last + 10**(l-1), l-1])
            last += 10**(l-1)
        else:
            l -= 1

    for s, e, l in intervals:
        if l != 0:
            e = s
        for n in range(s, e + 1):
            i = 1
            boring = True
            for d in str(n):
                if i % 2 != int(d) % 2:
                    boring = False
                i += 1
                if i > len(str(n)) - l:
                    break
            if boring and l == 0:
                lsum += 1

        if boring and l != 0:
            lsum += 5**l
    
    return rsum - lsum

solution = solution_fastest

tc = int(raw_input())
for i in xrange(1, tc + 1):
    L, R = raw_input().split()
    out = solution(int(L), int(R))
    print("Case #{}: {}".format(i, out))