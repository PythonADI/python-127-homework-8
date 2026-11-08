def count_letters(word):
    """Return a dictionary of how many times each letter appears."""
    counts = {}
    for letter in word:
        counts[letter] = counts.get ( letter, 0) +1  
    return counts

print(count_letters("banana"))
print(count_letters("a"))
print(count_letters(""))