import random

def load_tiles():
    with open("tiles.txt") as file:
        content = file.read().splitlines()
        return content

def generate_board():
    board = []
    tiles = load_tiles()
    random.shuffle(tiles)
    tiles.insert(12, "FREE")
    for row_index in range(5):
        start = row_index * 5
        end = start + 5
        row = tiles[start:end]
        board.append(row)
    
    return board
    #plan to shuffle here later on

if __name__ == "__main__":
    tiles = generate_board()
    print(tiles)