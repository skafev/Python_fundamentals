the_number = False
while not the_number:
    number = float(input())
    if 1 <= number <= 100:
        print(f'The number {number} is between 1 and 100')
        the_number = True