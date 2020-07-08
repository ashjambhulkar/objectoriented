def helper(cells, N):
    for _ in range(N):
        temp = []
        temp = cells[:1]
        for j in range(2, len(cells)):
            if (cells[j-2] == 1 and cells[j] == 1) or (cells[j-2] == 0 and cells[j] == 0):
                temp.append(1)
            else:
                temp.append(0)
        temp.append(0)
        cells = temp

    return cells


print(helper([0, 1, 0, 1, 1, 0, 0, 1], 7))
