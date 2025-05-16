from icecream import ic

def return_only_n_bits(x,n):
    return x & ((1<<n)-1)

def ones_complement(n, bits=8): 
    # Masking to keep only 'bits' number of bits
    return return_only_n_bits(~n)  

ic( ones_complement(5))