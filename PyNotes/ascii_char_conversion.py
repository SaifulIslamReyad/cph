from icecream import ic

# ==================== ASCII TO CHAR CONVERSION ====================

# 1. Basic chr() function - ASCII code to character
print("=== ASCII to Character ===")
ic(chr(65))  # 'A'
ic(chr(97))  # 'a'
ic(chr(48))  # '0'
ic(chr(32))  # ' ' (space)
ic(chr(33))  # '!'

# 2. Range of characters
print("\n=== Uppercase Letters ===")
for i in range(65, 91):  # A-Z
    print(f"{i}: {chr(i)}", end="  ")
print()

print("\n=== Lowercase Letters ===")
for i in range(97, 123):  # a-z
    print(f"{i}: {chr(i)}", end="  ")
print()

print("\n=== Digits ===")
for i in range(48, 58):  # 0-9
    print(f"{i}: {chr(i)}", end="  ")
print()

# ==================== CHAR TO ASCII CONVERSION ====================

# 3. Basic ord() function - Character to ASCII code
print("\n\n=== Character to ASCII ===")
ic(ord("A"))  # 65
ic(ord("a"))  # 97
ic(ord("0"))  # 48
ic(ord(" "))  # 32
ic(ord("Z"))  # 90
ic(ord("z"))  # 122

# ==================== PRACTICAL APPLICATIONS ====================


# 4. Check if character is uppercase
def is_uppercase(char):
    return 65 <= ord(char) <= 90


ic(is_uppercase("A"))  # True
ic(is_uppercase("a"))  # False


# 5. Check if character is lowercase
def is_lowercase(char):
    return 97 <= ord(char) <= 122


ic(is_lowercase("a"))  # True
ic(is_lowercase("A"))  # False


# 6. Check if character is digit
def is_digit(char):
    return 48 <= ord(char) <= 57


ic(is_digit("5"))  # True
ic(is_digit("a"))  # False


# 7. Convert case manually using ASCII
def to_uppercase(char):
    if is_lowercase(char):
        return chr(ord(char) - 32)  # a-z to A-Z (difference is 32)
    return char


def to_lowercase(char):
    if is_uppercase(char):
        return chr(ord(char) + 32)  # A-Z to a-z (difference is 32)
    return char


ic(to_uppercase("h"))  # 'H'
ic(to_lowercase("H"))  # 'h'


# 8. Caesar Cipher implementation
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if is_uppercase(char):
            # Shift within A-Z range
            shifted = ((ord(char) - 65 + shift) % 26) + 65
            result += chr(shifted)
        elif is_lowercase(char):
            # Shift within a-z range
            shifted = ((ord(char) - 97 + shift) % 26) + 97
            result += chr(shifted)
        else:
            result += char  # Keep non-alphabetic characters as is
    return result


ic(caesar_cipher("Hello World!", 3))  # "Khoor Zruog!"
ic(caesar_cipher("abc XYZ", 1))  # "bcd YZA"

# ==================== COMPETITIVE PROGRAMMING TRICKS ====================


# 9. Convert string of digits to integers
def string_digits_to_ints(s):
    return [ord(char) - 48 for char in s if is_digit(char)]


ic(string_digits_to_ints("a1b2c3"))  # [1, 2, 3]

# 10. Generate alphabet arrays quickly
lowercase_alphabet = [chr(i) for i in range(97, 123)]
uppercase_alphabet = [chr(i) for i in range(65, 91)]
ic(lowercase_alphabet[:5])  # ['a', 'b', 'c', 'd', 'e']
ic(uppercase_alphabet[:5])  # ['A', 'B', 'C', 'D', 'E']


# 11. Character frequency using ASCII as index
def char_frequency_array(s):
    # Create array for a-z (26 characters)
    freq = [0] * 26
    for char in s.lower():
        if is_lowercase(char):
            freq[ord(char) - 97] += 1
    return freq


text = "hello world"
freq = char_frequency_array(text)
for i, count in enumerate(freq):
    if count > 0:
        print(f"'{chr(i + 97)}': {count}")


# 12. Distance between characters
def char_distance(char1, char2):
    return abs(ord(char1) - ord(char2))


ic(char_distance("a", "z"))  # 25
ic(char_distance("A", "Z"))  # 25
ic(char_distance("a", "A"))  # 32

# ==================== USEFUL ASCII RANGES ====================

print("\n=== ASCII Reference ===")
ascii_ranges = {
    "Digits": (48, 57),  # '0' to '9'
    "Uppercase": (65, 90),  # 'A' to 'Z'
    "Lowercase": (97, 122),  # 'a' to 'z'
    "Space": (32, 32),  # ' '
    "Symbols": [(33, 47), (58, 64), (91, 96), (123, 126)],
}

for name, ranges in ascii_ranges.items():
    if name == "Symbols":
        print(f"{name}: Multiple ranges")
        for start, end in ranges:
            chars = "".join(chr(i) for i in range(start, end + 1))
            print(f"  {start}-{end}: {chars}")
    else:
        start, end = ranges
        chars = "".join(chr(i) for i in range(start, end + 1))
        print(f"{name}: {start}-{end} -> {chars}")

# ==================== ADVANCED TECHNIQUES ====================


# 13. Bitwise operations with ASCII
def toggle_case(char):
    """Toggle case using bitwise XOR (ASCII trick)"""
    if is_uppercase(char) or is_lowercase(char):
        return chr(ord(char) ^ 32)  # XOR with 32 flips case
    return char


ic(toggle_case("A"))  # 'a'
ic(toggle_case("a"))  # 'A'


# 14. Check if two characters are same case
def same_case(char1, char2):
    return (is_uppercase(char1) and is_uppercase(char2)) or (
        is_lowercase(char1) and is_lowercase(char2)
    )


ic(same_case("A", "B"))  # True
ic(same_case("a", "b"))  # True
ic(same_case("A", "b"))  # False


# 15. Get alphabetical position (1-indexed)
def get_position(char):
    if is_uppercase(char):
        return ord(char) - 64  # A=1, B=2, ..., Z=26
    elif is_lowercase(char):
        return ord(char) - 96  # a=1, b=2, ..., z=26
    return 0


ic(get_position("A"))  # 1
ic(get_position("Z"))  # 26
ic(get_position("a"))  # 1
ic(get_position("z"))  # 26

# ==================== COMMON PATTERNS FOR CP ====================


# Pattern 1: Count character frequencies
def count_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Pattern 2: Convert number to character (for encoding)
def num_to_char(num):
    return chr(num + ord("a"))  # 0->a, 1->b, etc.


# Pattern 3: Character matrix manipulation
def char_matrix_shift(matrix, shift):
    result = []
    for row in matrix:
        new_row = ""
        for char in row:
            if is_lowercase(char):
                new_char = chr(((ord(char) - 97 + shift) % 26) + 97)
                new_row += new_char
            else:
                new_row += char
        result.append(new_row)
    return result


# Example usage
matrix = ["abc", "def", "xyz"]
shifted = char_matrix_shift(matrix, 1)
ic("Original:", matrix)
ic("Shifted by 1:", shifted)

print("\n=== Quick Reference ===")
print("chr(65) = 'A'    |    ord('A') = 65")
print("chr(97) = 'a'    |    ord('a') = 97")
print("chr(48) = '0'    |    ord('0') = 48")
print("Uppercase: A-Z = 65-90")
print("Lowercase: a-z = 97-122")
print("Digits: 0-9 = 48-57")
print("Case difference = 32 (A=65, a=97)")
