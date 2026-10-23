board = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]


def printboard(board):
    for row in board:
        print(" | ".join(row))
        print('_ '*5)

def P1P():
    CP1 = 'X'

    while True:
        placeR = int(input("Player X - enter row (0-2): "))
        placeC = int(input("Player X - enter column (0-2): "))

        if placeR not in range(3) or placeC not in range(3):
            print("Invalid position! Choose 0, 1, or 2.")

        elif board[placeR][placeC] != " ":
            print("Cell is occupied! Try again.")

        else:
            board[placeR][placeC] = CP1
            break

def P2P():
    CP2='O'
    while True:
        placeR = int(input("Player 0 - enter row (0-2): "))
        placeC = int(input("Player 0 - enter column (0-2): "))

        if placeR not in range(3) or placeC not in range(3):
            print("Invalid position! Choose 0, 1, or 2.")

        elif board[placeR][placeC] != " ":
            print("Cell is occupied! Try again.")

        else:
            board[placeR][placeC] = CP2
            break

def Checkwinner():
    for r in board:
        if r[0]==r[1]==r[2]!=" ":
            return r[0]
    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]!=' ':
            return board[0][c]
    if board[0][0]==board[1][1]==board[2][2]!=' ':
        return board[1][1]
    if board[0][2]==board[1][1]==board[2][0]!=' ':
        return board[1][1]
    return None

while True:
    printboard(board)
    P1P()
    winner=Checkwinner()
    if winner:
        printboard(board)
        print(winner, "wins!")
        break
    printboard(board)
    P2P()
    winner=Checkwinner()
    if winner:
        printboard(board)
        print(winner, "wins!")
        break    

