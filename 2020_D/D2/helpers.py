l1 = [4,5,6,10,20,1]

def find_min(i):
    if i < 0:
        return l1[0]

    min_val = find_min(i - 1)
    min_val = min(min_val, l1[i])

    return min_val