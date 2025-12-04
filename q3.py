def solve_part1():
    with open('input_q3.txt', 'r') as f:
        lines = f.readlines()

    total_joltage = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        max_val = 0
        for d1_val in range(9, -1, -1):
            d1 = str(d1_val)
            idx = line.find(d1)
            
            if idx != -1 and idx < len(line) - 1:
                remaining = line[idx+1:]
                d2 = max(remaining)
                
                current_val = int(d1 + d2)
                max_val = current_val
                break
        
        total_joltage += max_val
        
    print(total_joltage)

def solve_part2():
    with open('input_q3.txt', 'r') as f:
        lines = f.readlines()

    total_joltage = 0
    K = 12
    
    for line in lines:
        line = line.strip()
        if len(line) < K:
            continue
            
        stack = []
        N = len(line)
        
        for i, digit in enumerate(line):
            while stack and stack[-1] < digit:
                if len(stack) - 1 + (N - i) >= K:
                    stack.pop()
                else:
                    break
            stack.append(digit)
            
        result = "".join(stack[:K])
        total_joltage += int(result)
        
    print(total_joltage)


if __name__ == "__main__":
    solve_part1()
    solve_part2()