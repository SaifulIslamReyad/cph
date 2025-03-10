from icecream import ic

def sqrt(x):
    if x == 0 or x == 1:
        return x

    l, h = 0, x
    ans = 0

    while l <= h:
        mid = (l + h) // 2  

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid 
            l = mid + 1
        else:
            h = mid - 1

    # Step 2: Find the fractional part using precision-based binary search
    # increment = 0.1
    # precision = 7
    # for _ in range(precision):  
    #     while ans * ans <= x:
    #         ans += increment
        
    #     ans -= increment  # Go back one step as it exceeded x
    #     increment /= 10  # Reduce increment for better precision


    # Step 2: Fractional part using binary search
    precision = 6
    l = ans
    h = ans + 1
    epsilon = 10 ** (-precision)

    while h>l :
        mid = (l + h) / 2
        num = mid * mid
        if abs(num - x) < epsilon:
            return round(mid, precision)
        elif num < x:
            l = mid + epsilon
        else:
            h = mid - epsilon

    return round(l, precision)





for _ in range(int(input())):
    print(sqrt(int(input())))
