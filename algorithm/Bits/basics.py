from icecream import ic

ic.disable()
AND = (13 & 7)
ic(AND , type(AND))

OR = (13 | 7)
ic(OR, type(OR))

XOR = (13 ^ 7)
ic(XOR, type(XOR))

RIGHT_SHIFT = (13 >> 2 )
ic(RIGHT_SHIFT, type(RIGHT_SHIFT))

def swap(a,b):
    a= a^b
    b= a^b  #  a^b^b = a
    a= a^b  #  a^b^a = b


def check_if_iTH_bit_set_or_not(n,i):
    if (n & (1<<i))!=0 : return True
    return False
ic(check_if_iTH_bit_set_or_not(13,0))

def check_if_iTH_bit_set_or_not2(n,i):
    if ((n>>i) & 1)!=0 : return True
    return False
ic(check_if_iTH_bit_set_or_not2(13,0))

def set_ith_bit(n,i):
    return (n | (1<<i))
ic(set_ith_bit(13,1))

def clear_ith_bit(n,i):
    return (n & ~(1<<i))
ic(clear_ith_bit(13,3))

def toggle_ith_bit(n,i):
    return n ^ (1<<i)
ic(toggle_ith_bit(13,2))

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
ic(count_set_bits(13))
ic(count_set_bits_efficient(13))
ic(count_set_bits_efficient_efficient(13))

def minimum_bit_flips_to_get_a_number_from_n_to_m(n,m):
    return count_set_bits_efficient_efficient((n^m))

ic.enable()
ic(minimum_bit_flips_to_get_a_number_from_n_to_m(0,3))