
def solve_part1():
    grid = []
    with open('input_q7.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())

    start_col = -1
    for c in range(len(grid[0])):
        if grid[0][c] == 'S':
            start_col = c
            break

    beams = {start_col}
    splits = 0
    width = len(grid[0])

    for r in range(1, len(grid)):
        next_beams = set()
        for c in beams:
            if c < 0 or c >= width:
                continue
            
            if grid[r][c] == '^':
                splits += 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)
            else:
                next_beams.add(c)
        beams = next_beams

    print(f"Part 1: {splits}")

def solve_part2():
    grid = []
    with open('input_q7.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())

    height = len(grid)
    width = len(grid[0])

    start_col = -1
    for c in range(width):
        if grid[0][c] == 'S':
            start_col = c
            break

    dp = [[0] * width for _ in range(height)]

    dp[0][start_col] = 1
    total_timelines = 0

    for r in range(height):
        for c in range(width):
            if dp[r][c] == 0:
                continue
            
            count = dp[r][c]
            cell = grid[r][c]
            
            if cell == 'S' or cell == '.':
                # Move down
                if r + 1 < height:
                    dp[r+1][c] += count
                else:
                    # Exits bottom
                    total_timelines += count
            elif cell == '^':
                # Split left
                if c - 1 >= 0:
                    if r + 1 < height:
                        dp[r+1][c-1] += count
                    else:
                        total_timelines += count
                else:
                    # Exits left
                    total_timelines += count
                
                # Split right
                if c + 1 < width:
                    if r + 1 < height:
                        dp[r+1][c+1] += count
                    else:
                        total_timelines += count
                else:
                    # Exits right
                    total_timelines += count

    print(f"Part 2: {total_timelines}")

if __name__ == "__main__":
    solve_part1()
    solve_part2()
