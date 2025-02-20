n = int(input()) - 1
while n > 4:
    n = (n - 5) >> 1
print(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][n])