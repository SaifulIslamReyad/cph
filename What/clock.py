from datetime import datetime
for _ in range(int(input())):
    s = input()
    dt = datetime.strptime(s, "%H:%M")
    print(dt.strftime("%I:%M %p"))