from icecream import ic
# A function that uses yield is called a generator function.
# ---------------------------------
# Instead of returning all values at once, it pauses execution 
# and remembers where it left off.
# -----------------------------------
# The next time the generator is used,
# execution resumes from where it stopped.

def numbers():  # generator function because it uses yield
    for i in range(1, 4):
        yield i
gen = numbers()  # Creates a generator object
ic(next(gen))  # Output: 1
ic(next(gen))  # Output: 2
ic(next(gen))  # Output: 3

# Here, yield produces values one at a time. 
# ----------------------------------------
# Instead of storing [1, 2, 3] in memory, 
# it pauses after each yield and resumes when next() is called.


# some examples
s= "saif_reyad"
ic(sum(s.count(consonant) for consonant in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"))
ic(sum(s.count(space) for space in " \t\n\r")) # Counts spaces, tabs (\t), newlines (\n), and carriage returns (\r) in s.
# ----------------------------------------------------------
ic(sum(1 for char in s if char in "AEIOUaeiou" )) #O(n)
ic(sum(s.count(vowel) for vowel in "AEIOUaeiou")) #O(10n)
#-----------------------------------------------------------
ic(max(s.count(vowel) for vowel in "AEIOUaeiou"))
ic(any(s.count(vowel) > 0 for vowel in "AEIOUaeiou")) #True if at least one vowel exists in s, otherwise False.
ic(all(s.count(vowel) > 0 for vowel in "AEIOUaeiou")) #Returns True only if all vowels appear at least once.
ic(sorted(s.count(vowel) for vowel in "AEIOUaeiou"))
# Returns a sorted list of vowel counts.
# Example: "Hello World" → [0, 0, 1, 1, 
ic(list(s.count(vowel) for vowel in "AEIOUaeiou"))
# Converts the generator into a list of counts.
# Example: "Hello" → [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]