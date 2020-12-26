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


def solution_fast(L, R):
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
        print(L)
        L = int(''.join([str(d) for d in a]))

    return count


def addition(L, R):
    """
    Adds two to an integer.
    """

    a = 999
    a = [int(d) for d in str(a)]
    i = len(a) - 1
    a[i] += 2
    c = a[i]

    while c >= 10:
        a[i] = c % 10
        i -= 1
        if i < 0:
            a = [0] + a
            i = 0
        a[i] += 1
        c = a[i]

    print(a)


def find_boring(L, R):
    N = 779
    A = [int(d) for d in str(N)]

    def is_even(n):
        return not n % 2

    i = len(A) - 1
    while i >= 0:
        if is_even(i + 1) != is_even(A[i]):
            A[i] += 1
            A[i - 1] += A[i] // 10
            A[i] = A[i] % 10
            A = A[:i + 1] + [0] * (len(A) - 1 - i)
            i = len(A) - 1
        else:
            A[i - 1] += A[i] // 10
            A[i] = A[i] % 10
            i -= 1

        if A[0] >= 10:
            A[0] = A[i] % 10
            A = [A[i] // 10] + A
            i += 1

    print(A)



solution = solution_fast

tc = int(raw_input())
for i in xrange(1, tc + 1):
    L, R = raw_input().split()
    out = solution(int(L), int(R))
    print("Case #{}: {}".format(i, out))