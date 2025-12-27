from icecream import ic
import math

x= 10
filling = bin(x)[2:].zfill(32)


AND = (13 & 7)
# ic(AND , type(AND))

OR = (13 | 7)
# ic(OR, type(OR))

XOR = (13 ^ 7)
# ic(XOR, type(XOR))

RIGHT_SHIFT = (13 >> 2 )
# ic(RIGHT_SHIFT, type(RIGHT_SHIFT))

def swap(a,b):
    a= a^b
    b= a^b  #  a^b^b = a
    a= a^b  #  a^b^a = b


def check_if_iTH_bit_set_or_not(n,i):
    if (n & (1<<i))!=0 : return True
    return False
# ic(check_if_iTH_bit_set_or_not(13,0))

def check_if_iTH_bit_set_or_not2(n,i):
    if ((n>>i) & 1)!=0 : return True
    return False
# ic(check_if_iTH_bit_set_or_not2(13,0))

def set_ith_bit(n,i):
    return (n | (1<<i))
# ic(set_ith_bit(13,1))

def clear_ith_bit(n,i):
    return (n & ~(1<<i))
# ic(clear_ith_bit(13,3))

def toggle_ith_bit(n,i):
    return n ^ (1<<i)
# ic(toggle_ith_bit(13,2))

def clear_the_last_occured_set_bit(n):
    return n&(n-1)

def check_if_num_is_pow_of_2(n):
    return n&(n-1)==0

def count_set_bits(n,c=0):
    while(n):
        if n%2==1: c+=1
        n//=2
    return c

def count_set_bits_efficient(n,c=0): #O(logn)
    while(n):
        c+= n & 1
        n>>=1
    return c
def count_set_bits_efficient_efficient(n, c=0): #O(c)
    while(n):
        n = n & (n-1)
        c+=1
    return c
# ic(count_set_bits(13))
# ic(count_set_bits_efficient(13))
# ic(count_set_bits_efficient_efficient(13))



def minimum_bit_flips_to_get_a_number_from_n_to_m(n,m):
    return count_set_bits_efficient_efficient((n^m))

# ic(minimum_bit_flips_to_get_a_number_from_n_to_m(0,3))



def powerset():
    SET = ["a","b","c","d"]
    n = len(SET)
    powerset = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)): #checks if index is 0 or 1
                subset.append(SET[j])
        powerset.append(subset)
    return powerset  

# time complexity O(n*2^n)
# space complexity O(n*2^n)



def find_single_element(L):  #all double one single
    n= len(L)
    ans= 0 
    # 00001
    # 00010
    # 00011 💕
    # 00001
    # 00010
    for i in range(n):
        ans= ans^L[i]
    return ans
# ic(find_single_element([1,2,2,3,4,3,4]))


def find_single_element2(L): #all triple one single
    ans=0
    n= len(L)
    for i in range(31): # assuming maximum bit will be 31
        c= 0 
        for j in range(n):
            if L[j] & (1<<i) : c+=1
        if c%3==1 : 
            ans = ans | (1<<i)
    return ans

# 0001
# 0001
# 0001
# 0010 💕
# 0011
# 0011
# 0011
# ic(find_single_element2([1,1,1,2,3,3,3]))


def find_length(x,c=0):
    while x: 
        x>>=1  
        c+=1
    return c
ic.enable()
ic(find_length(2))

def find_length_efficient(x):
    return int(math.log2(x))+1

def maximizingXor(l, r):
    return 2**(find_length_efficient(l^r))-1

def swap_adjacent_two_bits(n):
    a = int("10101010101010101010101010101010",2)
    b = int("01010101010101010101010101010101",2)
    aa= n & a
    bb= n & b
    aa >>= 1
    bb <<= 1
    return aa|bb


def reverse_bits(n):
    x= bin(n)[2::].zfill(32)
    x=x[::-1]
    return int(x,2)
L=list(map(int, input().split()))
for i in L[1::]:
    print(reverse_bits(i),end=" ")



def reverse_bits2(n):
    ans = 0
    for i in range(32):
        ans |= ((n >> i) & 1) << (31 - i)
    return ans
L = list(map(int, input().split()))
for i in L[1:]:
    print(reverse_bits2(i), end=" ")


def calculate_xor_from_1_to_n(n):
    # n= 100
    # for i in range(1,n+1):
    #     c=0
    #     for j in range(1,i+1):
    #         c^=j
    #     print(f"for {i=} ,{c= }") 
    # after finding the pattern 
    if n %4== 0 : return n
    if n %4== 1 : return 1
    if n %4== 2 : return n+1
    if n %4== 3 : return 0

def calculate_xor_of_range(right, left=1):
    return calculate_xor_from_1_to_n(right) ^ calculate_xor_from_1_to_n(left)
    # as 1^2^3^ (1^2^3^x^y) = x^y