def is_safe(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)

    valid_dif = all(1 <= abs(diff) <= 3 for diff in diffs)

    return (all_increasing or all_decreasing) and valid_dif


def count_with_dampener(filepath):
    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))

            if is_safe(report):
                count += 1
                continue

            for i in range(len(report)):
                modified = report[:i] + report[i + 1:]
                if is_safe(modified):
                    count += 1
                    break

    return count


file_path = "input_day2.txt"

safe_reports_number= count_with_dampener(file_path)
print(f" {safe_reports_number}")
