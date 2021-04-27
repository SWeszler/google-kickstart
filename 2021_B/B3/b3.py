def solution_bf(Z):
    return Z


solution = solution_bf


tc = int(input())
for i in range(1, tc + 1):
    Z = input()
    out = solution(int(Z))
    print("Case #{}: {}".format(i, out))