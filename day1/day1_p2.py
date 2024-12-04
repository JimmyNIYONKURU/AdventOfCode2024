from collections import Counter

def calculate_similarity_score(file_path):
    left_list, right_list = [], []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    right_count = Counter(right_list)

    print(f"Right list count: {right_count}")

    similarity_score = sum(left * right_count[left] for left in left_list)

    return similarity_score

file_path = "input_day1.txt"
result = calculate_similarity_score(file_path)
print(f"Similarity score: {result}")

