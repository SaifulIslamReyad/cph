for _ in range(int(input())):
    s=input()+ input() + input()
    a = s.count("A")
    b= s.count("B")
    c = s.count("C")
    if a==2 : print("A")
    if b==2: print('B')
    if c==2 : print("C")