text = input().split(" ")
team_A = 11
team_B = 11
less_then_seven = False
for text_one in set(text):
    if "A" in text_one:
        team_A -= 1
    if "B" in text_one:
        team_B -= 1
    if team_A < 7:
        less_then_seven = True
        break
    if team_B < 7:
        less_then_seven = True
        break
print(f"Team A - {team_A}; Team B - {team_B}")
if less_then_seven:
    print("Game was terminated")