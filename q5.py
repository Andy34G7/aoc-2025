
def solve_part1():
    with open('input_q5.txt', 'r') as f:
        content = f.read().strip()

    parts = content.split('\n\n')
    ranges_lines = parts[0].splitlines()
    ids_lines = parts[1].splitlines()

    ranges = []
    for line in ranges_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    ids = [int(line) for line in ids_lines]

    fresh_count = 0
    for id_val in ids:
        is_fresh = False
        for start, end in ranges:
            if start <= id_val <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    print(f"Fresh ingredients: {fresh_count}")

def solve_part2():
    with open('input_q5.txt', 'r') as f:
        content = f.read().strip()

    parts = content.split('\n\n')
    ranges_lines = parts[0].splitlines()

    ranges = []
    for line in ranges_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    ranges.sort(key=lambda x: x[0])

    merged = []
    if ranges:
        curr_start, curr_end = ranges[0]
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            if next_start <= curr_end + 1:
                curr_end = max(curr_end, next_end)
            else:
                merged.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        merged.append((curr_start, curr_end))

    total_fresh = sum(end - start + 1 for start, end in merged)
    print(f"Total fresh ingredients (ranges): {total_fresh}")

if __name__ == "__main__":
    solve_part1()
    solve_part2()
