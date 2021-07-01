skill = input()

while True:
    command = input().split(" ")
    if command[0] == "For" and command[1] == "Azeroth":
        break

    elif command[0] == "GladiatorStance":
        skill = skill.upper()
        print(skill)

    elif command[0] == "DefensiveStance":
        skill = skill.lower()
        print(skill)

    elif command[0] == "Dispel":
        index = command[1]
        letter = command[2]
        if int(index) >= len(skill):
            print("Dispel too weak.")
        else:
            skill = skill[:int(index)] + letter + skill[int(index) + 1:]
            print("Success!")

    elif command[0] == "Target" and command[1] == "Change":
        substring = command[2]
        second_substring = command[3]
        if substring in skill:
            skill = skill.replace(substring, second_substring, len(skill))
        print(skill)

    elif command[0] == "Target" and command[1] == "Remove":
        substring = command[2]
        if substring in skill:
            skill = skill.replace(substring, "")
        print(skill)

    else:
        print("Command doesn't exist!")
