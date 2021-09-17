board = list(range(1,10))

def draw_board(board):
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        


def main(board):
    draw_board(board)

main(board)