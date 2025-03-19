from functools import lru_cache

def count_vowels(s)-> int :
    return sum(s.count(vowel) for vowel in "AEIOUaeiou")