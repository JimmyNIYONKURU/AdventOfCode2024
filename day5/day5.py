from collections import defaultdict, deque

def read_input(filename):
    with open(filename) as f:
        rules, updates = f.read().split("\n\n")
        rule_list = [line.split("|") for line in rules.splitlines()]
        update_list = [list(map(int, line.split(","))) for line in updates.splitlines()]
    return rule_list, update_list


def build_graph(rule_list):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # graph de dépendances
    for pre, succ in rule_list:
        pre, succ = int(pre), int(succ)
        graph[pre].append(succ)
        indegree[succ] += 1
        if pre not in indegree:
            indegree[pre] = 0

    return graph, indegree


def check_order(update, graph, indegree):
    # mise à jour respectant l'ordre
    positions = {page: idx for idx, page in enumerate(update)}

    for pre in graph:
        for succ in graph[pre]:
            if succ in positions and pre in positions:
                if positions[pre] > positions[succ]:
                    return False
    return True


def calculate_middle_page(update):
    # page du milieu pour une update valide
    n = len(update)
    middle_idx = n // 2
    return update[middle_idx]


def main():
    rule_list, update_list = read_input("input_day5.txt")

    # graph de dépendances
    graph, indegree = build_graph(rule_list)

    # check les mises à jour et compute la somme des pges du milieu
    total_sum = 0
    for update in update_list:
        if check_order(update, graph, indegree):
            total_sum += calculate_middle_page(update)

    print(f"Total sum of middle pages: {total_sum}")


if __name__ == "__main__":
    main()


