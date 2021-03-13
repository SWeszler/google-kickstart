def solution_bf(W, H, L, U, R, D):
    return 0

solution = solution_bf

tc = input()

for i in range(1, int(tc) + 1):
    W, H, L, U, R, D = input().split()
    out = solution(int(W), int(H), int(L), int(U), int(R), int(D))
    print(f"Case #{i}: {out}")