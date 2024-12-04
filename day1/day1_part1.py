def calculate_total_distance_from_file(file_path):
    left_list, right_list = [], []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance


file_path = "input_day1.txt"
result = calculate_total_distance_from_file(file_path)
print(f"Total distance: {result}")
