def lcm(a, b):
    x=a
    y=b
    while b != 0:
        a, b = b, a % b
    return x*y//a


num1 = 36
num2 = 48
print(lcm(num1, num2))
