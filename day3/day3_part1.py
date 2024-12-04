import re
def sum_of_mul(file_path):
    total = 0
    # regex
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern, line)
            for x, y in matches:
                total += int(x) * int(y)

    return total
file_path = "input_day3.txt"

result = sum_of_mul(file_path)
print(f"{result}")
