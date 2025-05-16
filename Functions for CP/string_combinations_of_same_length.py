from itertools import permutations

def unique_digit_combinations(s):
    perm = set(permutations(s))
    return [int(''.join(p)) for p in perm]

print(unique_digit_combinations("1234"))