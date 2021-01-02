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