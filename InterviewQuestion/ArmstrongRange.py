def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(digit)**power for digit in str(num))

def find_armstrong_in_range(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]

print(find_armstrong_in_range(1, 1000))
