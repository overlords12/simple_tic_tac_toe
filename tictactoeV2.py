# Global Variables:
graph_input = " " * 9
numeric = [0 if i == " " else 1 if i == "X" else -1 for i in graph_input]
state = [numeric[i:i+3] for i in range(0, len(numeric), 3)]
X_O_turn = 1


def state_validate(state):
    # Not double turns:
    if (sum(sum(x) if isinstance(x, list)
            else x for x in state) in [-1, 0, 1]):
        rows = []
        columns = []
        diag_ppal = int((state[0][0] + state[1][1] + state[2][2]) / 3)
        diag_sec = int((state[2][0] + state[1][1] + state[0][2]) / 3)
        # Rows and Colums sums
        for i in range(0, 3):
            rows.append(state[i][0] + state[i][1] + state[i][2])
            columns.append(state[0][i] + state[1][i] + state[2][i])
        # Win conditions:
        if (rows.count(3) + rows.count(-3) + diag_ppal + diag_sec +
                columns.count(3) + columns.count(-3) in [-1, 1]):
            if (rows.count(3) == 1 or diag_ppal == 1 or diag_sec == 1 or
                    columns.count(3) == 1):
                return "X wins"
            else:
                return "O wins"
        elif (rows.count(3) + rows.count(-3) + diag_ppal + diag_sec
                + columns.count(3) + columns.count(-3) > 1):
            return "Impossible"
        # Game not finished:
        if 0 in [j for i in state for j in i]:
            return "Game not finished"
        elif 0 not in [j for i in state for j in i]:
            return "Draw"
    else:
        return "Impossible"


def graph_state(state):
    de_list = [j for i in state for j in i]
    graph = [" " if i == 0 else "X" if i == 1 else "O" for i in de_list]
    print("-" * 9)
    for i in range(0, 9, 3):
        print("| " + " ".join(graph[i:i + 3]) + " |")
    print("-" * 9)


def player_move(state):
    global X_O_turn
    validity = 0
    while validity < 3:
        validity = 0
        move = input("Enter the coordinates: ")
        if move.isnumeric:
            validity += 1
            move = [int(i) - 1 for i in list(move.split())]
            if 0 <= move[0] <= 2 and 0 <= move[1] <= 2:
                validity += 1
                if state[move[0]][move[1]] == 0:
                    validity += 1
                    if X_O_turn == 1 and validity == 3:
                        state[move[0]][move[1]] = 1
                        X_O_turn = -1
                    elif X_O_turn == -1 and validity == 3:
                        state[move[0]][move[1]] = -1
                        X_O_turn = 1
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3! ")
        else:
            print("You should enter numbers!")


graph_state(state)
while True:
    player_move(state)
    graph_state(state)
    a = state_validate(state)
    print(a)
    if a in ["Draw", "X wins", "O wins"]:
        break


print(int(-2/3))
