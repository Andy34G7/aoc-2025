def solve():
    with open('input_q4.txt', 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    def neighbors(i, j):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    yield grid[ni][nj]

    accessible = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '@':
                continue
            count_adj = sum(1 for c in neighbors(i, j) if c == '@')
            if count_adj < 4:
                accessible += 1
    print(accessible)


def solve_p2():
    with open('input_q4.txt', 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    def adjacent_at_count(i, j):
        count = 0
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                    count += 1
        return count

    total_removed = 0
    while True:
        accessible = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != '@':
                    continue
                if adjacent_at_count(i, j) < 4:
                    accessible.append((i, j))

        if not accessible:
            break

        total_removed += len(accessible)
        for i, j in accessible:
            grid[i][j] = '.'

    print(total_removed)


if __name__ == '__main__':
    solve()
    solve_p2()
