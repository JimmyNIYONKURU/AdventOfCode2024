def count_xmas(grid):
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Vérifier horizontalement et horizontal inversé
    for row in grid:
        count += row.count(word)  # Horizontal normal
        count += row[::-1].count(word)  # Horizontal inversé

    # Vérifier verticalement et vertical inversé
    for col in range(len(grid[0])):
        vertical = ''.join(row[col] for row in grid)
        count += vertical.count(word)  # Vertical normal
        count += vertical[::-1].count(word)  # Vertical inversé

    # Vérifier les diagonales (les deux directions)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Diagonale bas-droite
            if row + word_len <= len(grid) and col + word_len <= len(grid[0]):
                diagonal_down_right = ''.join(grid[row+i][col+i] for i in range(word_len))
                count += diagonal_down_right.count(word)
                count += diagonal_down_right[::-1].count(word)
            # Diagonale bas-gauche
            if row + word_len <= len(grid) and col - word_len >= -1:
                diagonal_down_left = ''.join(grid[row+i][col-i] for i in range(word_len))
                count += diagonal_down_left.count(word)
                count += diagonal_down_left[::-1].count(word)

    return count

def read_file(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

# Lire le fichier et calculer le résultat
file_path = 'inputday3.txt'  # Remplacez par le chemin de votre fichier
grid = read_file(file_path)
result = count_xmas(grid)
print(f" {result}")
