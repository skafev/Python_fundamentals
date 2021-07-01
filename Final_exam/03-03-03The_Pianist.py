number_of_pieces = int(input())
pieces = {}

for n in range(number_of_pieces):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    pieces[piece] = {}
    pieces[piece]["composer"] = composer
    pieces[piece]["key"] = key

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break

    piece = command[1]

    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece not in pieces:
            pieces[piece] = {}
            pieces[piece]["composer"] = composer
            pieces[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        new_piece = command[2]
        if piece in pieces:
            pieces[piece]["key"] = new_piece
            print(f"Changed the key of {piece} to {new_piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

sorted_collection = sorted(pieces.keys(), key=lambda p: (p, pieces[p]["composer"]))
for i in sorted_collection:
    print(f"{i} -> Composer: {pieces[i]['composer']}, Key: {pieces[i]['key']}")
