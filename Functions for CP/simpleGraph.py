l = [1]
ll = []
for _ in range(int(input())):
    for i in l:
        ll.append(i*2)
        ll.append(i*3)
    l = ll
    ll = []

print(l)



l = [0]
ll = []
for _ in range(int(input())):
    n = int(input())
    for i in l:
        ll.append((i + n) % 360)
        ll.append((i - n) % 360)
    l = ll
    ll = []

print("YES" if 0 in l else "NO")
