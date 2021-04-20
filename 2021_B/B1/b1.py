
def solution(N, S):
    store = {}
    count = 1
    for i in range(N):
        if i > 0 and ord(S[i]) > ord(S[i - 1]):
            count += 1
        else:
            count = 1
        store[i] = count

    return " ".join([str(i) for i in store.values()])



tc = int(input())
for i in range(1, tc + 1):
    L = input()
    S = input()
    out = solution(int(L), S)
    print("Case #{}: {}".format(i, out))
