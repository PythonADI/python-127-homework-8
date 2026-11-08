def count_letters(word):
    """Return a dictionary of how many times each letter appears."""
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1            #ერთ ხაზში ვერ მოვიფიქრე როგორ
        else:
            counts[letter] = 1

    return counts

print(count_letters("Banana"))
print(count_letters("a"))
print(count_letters(""))
