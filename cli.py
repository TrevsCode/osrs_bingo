from board import generate_board

def main():
    num_boards = int(input("How many bingo boards would you like to generate? "))
    for i in range(num_boards):
        board = generate_board()
        for row in board:
            row_string = " | ".join(row)
            print(row_string)
        print("--------------------------------")


if __name__ == "__main__":
    main()
