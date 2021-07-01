class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}")


mails = []
while True:
    text = input()
    if text == "Stop":
        break
    data = text.split()
    sender = data[0]
    receiver = data[1]
    content = data[2]
    a = Email(sender, receiver, content)
    mails.append(a)

to_send = list(map(lambda x: int(x), input().split(", ")))
for x in to_send:
    mails[x].send()

for a in mails:
    a.get_info()
