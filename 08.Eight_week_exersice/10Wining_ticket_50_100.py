tickets = input().replace(", ", " ").split()
winning_symbols = "@", "#", "$", "^"
symbols = ""
left_side = ""
right_side = ""
symbol = ""
for ticket in tickets:
    if len(ticket) < 20 or len(ticket) > 20:
        print("invalid ticket")
        continue
    if ticket == 20 * "@" or ticket == 20 * "#" or ticket == 20 * "$" or ticket == 20 * "^":
        for ch in ticket:
            symbol = ch
        print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
        continue
    for ch in ticket:
        if ch.isalpha():
            if symbols == "":
                continue
            else:
                if left_side == "":
                    left_side += symbols
                else:
                    right_side += symbols
                symbols = ""
        elif ch in winning_symbols:
            symbol = ch
            symbols += symbol

    if len(left_side) >= 6 and len(right_side) >= 6:
        bigger = len(left_side)
        if len(right_side) > len(left_side):
            bigger = len(right_side)
        print(f'ticket "{ticket}" - {bigger}{symbol}')
    if symbol == "":

        print(f'ticket "{ticket}" - no match')
