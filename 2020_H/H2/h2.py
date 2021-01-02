def solution(L, R):
    intervals = []
    l = 1
    last = 0
    rsum = 0
    lsum = 0
    
    while last < R and l > 0:
        if R - last < 10:
            intervals.append([last + 1, R, 0])
            break
        elif 10**l - 10**(l-1) <= R - last:
            intervals.append([last + 1, last + 10**l - 10**(l-1), l])
            last += 10**l - 10**(l-1)
            l += 1
        elif 10**(l-1) <= R - last:
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
    while last < L - 1 and l > 0:
        if L - last < 10:
            intervals.append([last + 1, L - 1, 0])
            break
        elif 10**l - 10**(l-1) <= L - last:
            intervals.append([last + 1, last + 10**l - 10**(l-1), l])
            last += 10**l - 10**(l-1)
            l += 1
        elif 10**(l-1) <= L - last:
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


tc = int(input())
for i in range(1, tc + 1):
    L, R = input().split()
    out = solution(int(L), int(R))
    print("Case #{}: {}".format(i, out))