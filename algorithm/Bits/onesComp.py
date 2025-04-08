def ones_complement(n, bits=8): return (~n) & ((1 << bits) - 1)  # Masking to keep only 'bits' number of bits

# Example: 8-bit 1's complement
num = 5  # Binary: 00000101
bits = 8
result = ones_complement(num, bits)
print(f"1's complement of {num} (binary {num:08b}) is {result} (binary {result:08b})")
