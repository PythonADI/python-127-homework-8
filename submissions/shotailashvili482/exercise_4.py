def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def most_common(counts):
    common = ''
    highest = 0
    for word, quantity in counts.items():
        if quantity > highest:
            common = word
            highest = quantity
    return (common, highest)

words = ["the", "cat", "and", "the", "dog", "and", "the", "bird"]
counts = count_words(words)
print(counts)
word, times = most_common(counts)
print(f"Most common: {word} ({times} times)")
print(most_common({"a": 2, "b": 2}))
print(count_words([]))