
def solve():
    with open('input_q6.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    if not lines:
        return

    token_rows = [line.split() for line in lines]
    problems = zip(*token_rows)
    
    grand_total = 0
    
    for problem in problems:
        operator = problem[-1]
        number_tokens = problem[:-1]
        
        numbers = [int(t) for t in number_tokens]
        
        if operator == '+':
            res = sum(numbers)
        elif operator == '*':
            res = 1
            for n in numbers:
                res *= n
        
        grand_total += res

    print(f"Part 1: {grand_total}")

def solve_part2():
    with open('input_q6.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    if not lines:
        return

    token_rows = [line.split() for line in lines]
    problems = zip(*token_rows)
    
    grand_total = 0
    
    for problem in problems:
        operator = problem[-1]
        number_tokens = problem[:-1]
        
        max_len = max(len(t) for t in number_tokens)
        cols = [""] * max_len
        
        if operator == '+':
            for token in number_tokens:
                for i, char in enumerate(token):
                    cols[i] += char
        elif operator == '*':
            for token in number_tokens:
                offset = max_len - len(token)
                for i, char in enumerate(token):
                    cols[offset + i] += char
        
        numbers = []
        for col_str in cols:
            if col_str:
                numbers.append(int(col_str))
        
        if operator == '+':
            res = sum(numbers)
        elif operator == '*':
            res = 1
            for n in numbers:
                res *= n
        
        grand_total += res

    print(f"Part 2: {grand_total}")

if __name__ == "__main__":
    solve()
    solve_part2()
