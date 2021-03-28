def solution(R, C, m):
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
                    graph[f"{r}{c}"] = nodes
    
    print(graph)


tc = int(input())
for i in range(1, tc + 1):
    R, C = input().split()
    m = []
    for k in range(int(R)):
        m.append([int(p) for p in input().split()])
    out = solution(int(R), int(C), m)
    print("Case #{}: {}".format(i, out))