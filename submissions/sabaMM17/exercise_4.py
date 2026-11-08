def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def most_common(counts):
    if not counts:
        return None
    
    best_word = None
    max_count = 0 
    
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            best_word = word

            
    return (best_word, max_count)

words = ["the", "cat", "and", "the", "dog", "and", "the", "bird"]
counts = count_words(words)
print(counts)
word, times = most_common(counts)
print(f"Most common: {word} ({times} times)")
print(most_common({"a": 2, "b": 2}))
print(count_words([]))