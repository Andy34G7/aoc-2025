import sys

def get_ranges(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    parts = [p for p in content.split(',') if p.strip()]
    ranges = []
    max_val = 0
    
    for p in parts:
        start, end = p.split('-')
        start, end = int(start), int(end)
        ranges.append((start, end))
        if end > max_val:
            max_val = end
    return ranges, max_val

def solve_part1():
    filename = 'input_q2.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    ranges, max_val = get_ranges(filename)
    max_digits = len(str(max_val))
    
    invalid_ids = []
    max_half_len = (max_digits + 1) // 2 
    
    for L in range(1, max_half_len + 1):
        start_half = 10**(L-1)
        end_half = 10**L - 1
        
        for half in range(start_half, end_half + 1):
            s_half = str(half)
            candidate_str = s_half + s_half
            candidate = int(candidate_str)
            
            in_any_range = False
            for start, end in ranges:
                if start <= candidate <= end:
                    in_any_range = True
                    break
            
            if in_any_range:
                invalid_ids.append(candidate)
                
    total_sum = sum(invalid_ids)
    print(total_sum)

def solve_part2():
    filename = 'input_q2.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    ranges, max_val = get_ranges(filename)
    max_digits = len(str(max_val))
    
    invalid_ids = set()
    
    max_s_len = max_digits // 2
    
    for L in range(1, max_s_len + 1):
        start_s = 10**(L-1)
        end_s = 10**L - 1
        
        for s_val in range(start_s, end_s + 1):
            s_str = str(s_val)
            
            k = 2
            while True:
                candidate_str = s_str * k
                if len(candidate_str) > max_digits:
                    break
                
                candidate = int(candidate_str)
                
                if candidate > max_val:
                    break
                
                in_any_range = False
                for r_start, r_end in ranges:
                    if r_start <= candidate <= r_end:
                        in_any_range = True
                        break
                
                if in_any_range:
                    invalid_ids.add(candidate)
                
                k += 1
                
    total_sum = sum(invalid_ids)
    print(total_sum)

if __name__ == "__main__":
    solve_part1()
    solve_part2()
