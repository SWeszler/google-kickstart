def solution(s):
    i = 0
    count_k = 0
    count_s = 0
    count = 0
    for i in range(len(s)):
        if s[i:i+4] == 'KICK':
            count_k += 1
        if s[i:i+5] == 'START':
            count_s += 1
        
        if count_s:
            count += count_k * count_s
            count_s = 0

    return count


tc = int(input())
for i in range(1, tc + 1):
    s = input()
    out = solution(s)
    print("Case #{}: {}".format(i, out))