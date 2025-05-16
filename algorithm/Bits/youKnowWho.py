# def flippingBits(n):
#     return ((1<<32) -1) ^ n 
# print(flippingBits(2147483647))


# def swap_adjacent_two_bits(n):
#     a = int("10101010101010101010101010101010",2)
#     b = int("01010101010101010101010101010101",2)
#     aa= n & a
#     bb= n & b
#     aa >>= 1
#     bb <<= 1
#     return aa|bb
# L=list(map(int, input().split()))
# n= len(L)
# for i in range(1,n):
#     print(swap_adjacent_two_bits(L[i]), end= " ")



# def reverse_bits(n):
#     x= bin(n)[2::].zfill(32)
#     x=x[::-1]
#     return int(x,2)
# L=list(map(int, input().split()))
# for i in L[1::]:
#     print(reverse_bits(i),end=" ")



# def reverse_bits2(n):
#     ans = 0
#     for i in range(32):
#         ans |= ((n >> i) & 1) << (31 - i)
#     return ans
# L = list(map(int, input().split()))
# for i in L[1:]:
#     print(reverse_bits2(i), end=" ")


# print(2**(int(input()))%1000000007)


    
# def powerset(string):
#     SET = list(string)
#     n = len(string)
#     powerset = []
#     for i in range(2**n):
#         subset = ""
#         for j in range(n):
#             if (i & (1 << j)): 
#                 subset+=SET[j]
#         powerset.append(subset)
#     return powerset  

# print(powerset("abcd"))

# def reyad(string,i,j):
#     saif= bin(i)[2:].zfill(j)
#     s=""
#     for ii in range(j): 
#         if saif[ii]=="1" : 
#             s+=string[ii]
#     print(s, end=" ")
#     if i<2**j-1 : reyad(string,i+1,j)
#     return 
# def allpossiblesubseq(string):
#     reyad(string,1,len(string))
#     return
# allpossiblesubseq("abcd")

# 925

# 500 235 175 120 15 6
# 6 15 120 175 235 500 
# from icecream import ic

import bisect
def bar(L,n):
        L.sort()
        while L :
            x= bisect.bisect_right(L,n)-1
            if n==0: f=1; break
            if x==-1 or n<0: f=0; break
            m = L.pop(x)
            n-= m
        return f
for _ in range(int(input())):
    n=int(input())
    m=int(input())
    L=list(map(int, input().split()))
    f= bar(L,n)
    print("YES" if f else 'NO')
