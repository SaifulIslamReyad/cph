from icecream import ic

def convert_to_bin(x):
    s=""
    while x:
        div = x%2
        s+= str(div)
        x = x//2
    return s[::-1]
# ic(convert_to_bin(5))
# print(f"{convert_to_bin(5) = }")


def convert_to_dec(s):
    s= s[::-1] #n
    n = len(s) 
    ans = 0
    for i in range(n):
        ans += int(s[i])*(2**i) #n
    return ans
# ic(convert_to_dec("1000"))

def convert_to_dec_efficient(s):
    return int(s, 2) 
    #O(n) but takes less time than my code as constant factor is reduced 

def convert_to_bin_efficient(n):
    return bin(n)[2:]
# ic(convert_to_dec_efficient("1000"))
# ic(convert_to_bin_efficient(9))



# Let's break down what these two lines of Python code do:

print(bin(-6 & 0xFF))
print(bin(-6))
# ### Code:

# ```python
# print(bin(-6 & 0xFF))
# print(bin(-6))
# ```

# ---

# ### Line 1: `print(bin(-6 & 0xFF))`

# * `-6 & 0xFF`: This performs a **bitwise AND** between `-6` and `0xFF` (which is `255` in decimal).
# * In Python, integers are of infinite length, but for the sake of bitwise operations, the values are treated as two's complement with a default word size (usually 32 or 64 bits).

# To calculate:

# * `-6` in binary (32-bit two's complement): `11111111 11111111 11111111 11111010`
# * `0xFF` in binary: `00000000 00000000 00000000 11111111`
# * AND operation gives: `00000000 00000000 00000000 11111010` = `250`

# So,

# ```python
# print(bin(-6 & 0xFF))  # Output: '0b11111010'
# ```

# ---

# ### Line 2: `print(bin(-6))`

# * Simply gives the **binary representation of `-6`**:

# ```python
# print(bin(-6))  # Output: '-0b110'
# ```

# Python represents negative numbers with a `-` sign followed by the binary of the absolute value.

# ---

# ### Final Output:

# ```
# 0b11111010
# -0b110
# ```

# Would you like a visualization of how two's complement works?
