import sys

def solution_bf(W, N, nums):
    m = float("inf")

    for x in range(1, N + 1):
        count = 0
        for n in nums:
            count += min(abs(x - n), N - x + n, N - n + x)
        m = min(m, count)

    return m


def solution_bf1(W, N, nums):
    m = float("inf")

    for n1 in nums:
        count = 0
        for n2 in nums:
            count += min(abs(n1 - n2), N - n1 + n2, N - n2 + n1)
        m = min(m, count)

    return m


def solution_fast(W, N, nums):
    m = float("inf")
    nums.sort()
    presum = [0]

    for i, n in enumerate(nums):
        presum.append(presum[i] + n)

    def get_sum(i, j):
        return presum[j] - presum[i]

    for i, n in enumerate(nums):
        l = 0
        r = i
        p = 0
        b = W
        count = 0

        while l <= r:
            mid = (l + r) // 2
            if N - n + nums[mid] >= n - nums[mid]:
                p = mid
                r = mid - 1
            else:
                l = mid + 1

        count += p * (N - n) + get_sum(0, p)
        count += (i - p) * n - get_sum(p, i)

        l = i + 1
        r = W - 1

        while l <= r:
            mid = (l + r) // 2
            if N - nums[mid] + n <= nums[mid] - n:
                b = mid
                r = mid - 1
            else:
                l = mid + 1
        
        count += (b - i) * -n + get_sum(i, b)
        count += (W - b) * (N + n) - get_sum(b, W)

        m = min(m, count)

    return m


solution = solution_fast

tc = int(raw_input())
for i in xrange(1, tc + 1):
    W, N = raw_input().split()
    nums = [int(n) for n in raw_input().split()]
    out = solution(int(W), int(N), nums)
    print("Case #{}: {}".format(i, out))