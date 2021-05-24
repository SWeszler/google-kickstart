def solution_bf(Z):

    def is_prime(x):
        if x in [0,1]:
            return False

        res = True
        for i in range(2, x):
            if x % i == 0:
                res = False
                break
        return res

    first = 2
    second = 3
    while first * second <= Z:
        last_first = first
        last_second = second
        first = second
        for i in range(first + 1, Z):
            if is_prime(i):
                second = i
                break


    return last_first * last_second


solution = solution_bf


tc = int(input())
for i in range(1, tc + 1):
    Z = input()
    out = solution(int(Z))
    print("Case #{}: {}".format(i, out))