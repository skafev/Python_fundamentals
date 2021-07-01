def integer_number(number):
    res = number * 2
    return res


def double_number(number):
    res = number * 1.5
    return res


def string(command):
    res = f"${command}$"
    return res


data = input()
command = input()

if data== "int":
    command = int(command)
    print(integer_number(command))

elif data == "real":
    command = float(command)
    print(f"{double_number(command):.2f}")

elif data == "string":
    print(string(command))