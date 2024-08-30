def print_field(field: list[list[str]]) -> None:
    print(*[' '.join(row) for row in field], sep='\n')


def get_move(field: list[list[str]], valid: frozenset[str]) -> list[int]:
    while True:
        while (move := input("Введите номер строки и столбца без пробелов:")) not in valid:
            print("Недопустимый ход.", end=' ')

        i, j = int(move[0]), int(move[1])
        if field[i][j] == '-':
            return [i, j]

        print("Клетка уже занята.", end=' ')


valid_moves = frozenset(["11", "12", "13", "21", "22", "23", "31", "32", "33"])
win_scores = frozenset([7, 56, 448, 73, 146, 292, 273, 84])


def play() -> None:
    plyer_scores = [0, 0]
    field = [[' ', '1', '2', '3'],
             ['1', '-', '-', '-'],
             ['2', '-', '-', '-'],
             ['3', '-', '-', '-']]

    print_field(field)
    for i in range(9):
        print(f"Ход игрока {1 + i % 2}.")

        r, c = get_move(field, valid_moves)
        field[r][c] = ['x', 'o'][i % 2]
        print_field(field)

        plyer_scores[i % 2] += 1 << (3 * r + c - 4)
        if plyer_scores[i % 2] in win_scores:
            return print(f"Конец игры.Игрок {1 + i % 2} победил")

    return print("Конец игры.Ничья")


sep = "-" * 100 + '\n' + ' ' * 50 + 'Новая Игра' + ' ' * 50 + '\n' + "-" * 100
while True:
    print(sep)
    play()

