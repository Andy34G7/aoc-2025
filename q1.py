input = open('d1pt1-input.txt', 'r')
dial = 50
count = 0
while True:
    line = input.readline()
    if not line:
        break
    direction = line[0]
    value = int(line[1:].strip())
    if direction == 'L':
        sign = -1
    else:
        sign = 1
    dial += sign * value
    dial %= 100
    if dial == 0:
        count += 1
input.close()
print(count)

# pt 2
input = open('d1pt1-input.txt', 'r')
dial = 50
count = 0
while True:
    line = input.readline()
    if not line:
        break
    direction = line[0]
    value = int(line[1:].strip())
    if direction == 'L':
        sign = -1
    else:
        sign = 1
    count += value // 100
    rem = value % 100
    if direction == 'L':
        if dial > 0 and dial - rem <= 0:
            count += 1
    else:
        if dial + rem >= 100:
            count += 1
            
    dial += sign * value
    dial %= 100

input.close()
print(count)