def solution_bf(R, C, m):
    auxm = [[c for c in r] for r in m]
    result = 0

    for i in range(1, R):
        for j in range(C):
            auxm[i][j] += auxm[i - 1][j]

    for i in range(R):
        for j in range(1, C):
            auxm[i][j] += auxm[i][j - 1]

    def segment_val(a, b, c, d):
        if d < b or c < a:
            a, c = c, a
            b, d = d, b
        res = auxm[c][d]
        if a > 0:
            res -= auxm[a - 1][d]
        if b > 0:
            res -= auxm[c][b - 1]
        if a > 0 and b > 0:
            res += auxm[a - 1][b - 1]
        return res
    
    for i in range(R):
        for j in range(C):
            for k in range(i + 1, R):
                for l in range(C):
                    hor = abs(j - l) + 1
                    ver = abs(i - k) + 1
                    sleft = segment_val(i, j, k, j)
                    sright = segment_val(i, l, k, l)
                    stop = segment_val(i, j, i, l)
                    sbottom = segment_val(k, j, k, l)

                    if ver > 1 and hor > 1 and (ver == 2 * hor or hor == 2 * ver):
                        if stop == hor and sright == ver:
                            result += 1
                        if sleft == ver and sbottom == hor:
                            result += 1
    return result


def solution_optimal(R, C, m):
    graph = {}
    
    for r in range(R):
        m[r] = [0] + m[r] + [0]

    empty = [0 for i in range(R + 1)]
    m = [empty] + m + [empty]

    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if m[r][c]:
                nodes = []
                if m[r - 1][c] and (m[r][c + 1] or m[r][c - 1]):
                    nodes.append([r - 1, c])
                if m[r + 1][c] and (m[r][c + 1] or m[r][c - 1]):
                    nodes.append([r + 1, c])
                if m[r][c - 1] and (m[r - 1][c] or m[r + 1][c]):
                    nodes.append([r, c - 1])
                if m[r][c + 1] and (m[r - 1][c] or m[r + 1][c]):
                    nodes.append([r, c + 1])
                
                if len(nodes) >= 2:
                    graph["{}{}".format(r, c)] = nodes
    
    print(graph)


solution = solution_bf


tc = int(input())
for i in range(1, tc + 1):
    R, C = raw_input().split()
    m = []
    for k in range(int(R)):
        m.append([int(p) for p in raw_input().split()])
    # if i != 2:
    #     continue
    out = solution(int(R), int(C), m)
    print("Case #{}: {}".format(i, out))