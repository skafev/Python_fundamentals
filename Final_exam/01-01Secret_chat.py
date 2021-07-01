message = input()
while True:
    command = input()
    instructions = command.split(":|:")

    if instructions[0] == "Reveal":
        break

    elif instructions[0] == "InsertSpace":
        index = int(instructions[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif instructions[0] == "Reverse":
        substring = instructions[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            new_substring = substring[::-1]
            message = message[::] + new_substring
            print(message)
        else:
            print("error")

    elif instructions[0] == "ChangeAll":
        ss, new_ss = instructions[1], instructions[2]
        if ss in message:
            message = message.replace(ss, new_ss, len(message))
        print(message)

print(f"You have a new text message: {message}")
