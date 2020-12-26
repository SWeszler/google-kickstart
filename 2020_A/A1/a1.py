from typing import List

def solution(houses: int, budget: int, prices: List[int]):
    res = 0
    total = 0
    prices.sort(reverse = True)
    while total < budget and prices:
        h = prices.pop()
        if budget - total >= h:
            res += 1
            total += h

    return res


tc = int(input())
for i in range(1, tc + 1):
    n, b = input().split()
    prices = input().split()
    out = solution(int(n), int(b), [int(p) for p in prices])
    print("Case #{}: {}".format(i, out))
