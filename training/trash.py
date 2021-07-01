first_line = input().split()
first_line = [int(i) for i in first_line]
second_line = input().split()
second_line = [int(i) for i in second_line]
third_line = input().split()
third_line = [int(i) for i in third_line]
empty_space = 0
first_player = 1
second_player = 2
index = 0

if first_line[index] == first_player or second_line[index] == first_player or third_line[index] == first_player:
    if first_line[index + 1] and first_line[index + 2] == first_player:
        print("First player won")
    elif second_line[index] and third_line[index] == first_player:
        print("First player won")
    elif second_line[index + 1] and third_line[index + 2] == first_player:
        print("First player won")
if first_line[index + 1] == first_player or first_line[index + 1] == second_player:
    if second_line[index + 1] == first_player and third_line[index + 1] == first_player:
        print("First player won")
    elif second_line[index + 1] == second_player and third_line[index + 1] == second_player:
        print("Second player won")
if first_line[index + 2] == first_player or first_line[index + 2] == second_player:
    if second_line[index + 2] and third_line[index + 2] == first_player:
        print("First player won")
    elif second_line[index + 2] and third_line[index + 2] == second_player:
        print("Second player won")


elif first_line[index] == second_player or second_line[index] == second_player or third_line[index] == second_player:
    if first_line[index + 1] and first_line[index + 2] == second_player:
        print("Second player won")
    elif second_line[index] and third_line[index] == second_player:
        print("Second player won")
    elif second_line[index + 1] and third_line[index + 2] == second_player:
        print("Second player won")
else:
    print("Draw")