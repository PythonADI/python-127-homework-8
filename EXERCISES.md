# Exercises

Create these files inside your own folder:
`submissions/<your-github-username>/`.

Give every function you write a one-line docstring saying what it
returns or does.

## exercise_1.py — Phone book

Start with exactly this dictionary:

```python
phones = {"Nina": "555-1234", "Luka": "555-9876"}
```

Then, in this order:

1. Print Luka's number using square brackets.
2. Print Ana's number using `.get()` with the default `"unknown"` (Ana
   is not in the phone book yet).
3. Add Ana with the number `"555-0000"`.
4. Change Nina's number to `"555-1111"`.
5. Use `in` to check whether `"Luka"` is a key, and print the result.
6. Remove Luka with `pop()` and print `Removed: <number>`.
7. Print the dictionary, then print how many contacts it has using
   `len()`.

Expected output:
```
Luka: 555-9876
Ana: unknown
Has Luka: True
Removed: 555-9876
{'Nina': '555-1111', 'Ana': '555-0000'}
2 contacts
```

## exercise_2.py — Fix the bug

This code should count the letters in each word. Instead it crashes
with `KeyError: 'b'`. Copy it into `exercise_2.py`, then fix the
function. Change only the line with the `BUG` comment.

```python
def count_letters(word):
    """Return a dictionary of how many times each letter appears."""
    counts = {}
    for letter in word:
        counts[letter] += 1   # BUG: fix this line
    return counts

print(count_letters("banana"))
print(count_letters("a"))
print(count_letters(""))
```

Expected output:
```
{'b': 1, 'a': 3, 'n': 2}
{'a': 1}
{}
```

## exercise_3.py — Corner shop

Start with this dictionary of prices:

```python
prices = {"bread": 2.5, "milk": 3.0, "cheese": 9.0}
```

Write three functions:

- `print_menu(prices)` prints every item and its price, one per line,
  as `item: price`. Loop with `.items()`.
- `cart_total(prices, cart)` takes a cart — a dictionary of
  `item: quantity` — and returns the total cost. Skip any item that is
  not in `prices` (use `in`).
- `cheapest(prices)` returns the **name** of the cheapest item. If two
  items tie, return the first one. Do **not** use `min()` in this
  exercise.

Then call them like this:

```python
print_menu(prices)
cart = {"bread": 2, "cheese": 1, "apples": 3}
print(cart_total(prices, cart))
print(cart_total(prices, {}))
print(cheapest(prices))
print(cheapest({"tea": 4.0, "coffee": 4.0}))
```

Expected output:
```
bread: 2.5
milk: 3.0
cheese: 9.0
14.0
0
bread
tea
```

## exercise_4.py — Word counter

Write two functions:

- `count_words(words)` takes a list of words and returns a dictionary
  of how many times each word appears.
- `most_common(counts)` takes such a dictionary and returns a
  **tuple** `(word, count)` for the word that appears most often. If
  two words tie, return the first one. Do **not** use `max()` in this
  exercise.

Then call them like this — note how the tuple is unpacked into two
variables:

```python
words = ["the", "cat", "and", "the", "dog", "and", "the", "bird"]
counts = count_words(words)
print(counts)
word, times = most_common(counts)
print(f"Most common: {word} ({times} times)")
print(most_common({"a": 2, "b": 2}))
print(count_words([]))
```

Expected output:
```
{'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
Most common: the (3 times)
('a', 2)
{}
```

## exercise_5.py — Bonus: class vote

Write a function `read_votes()` that keeps asking for names and
**returns** a dictionary counting how many votes each name got. Each
time it asks, it first prints `Vote (or done):` on its own line and
then calls `input()` with **no prompt text**. When the user types
`done`, return the dictionary.

Write a second function `report(votes)` that prints every name with
its number of votes (in the order they first got a vote), and then
`Winner: <name>` — the name with the most votes. If two names tie,
the winner is the one that got its first vote earlier. If the
dictionary is empty, it prints `No votes.` instead (return early).

Then use them like this:

```python
votes = read_votes()
report(votes)
```

Run it and type these five values, one per line, pressing Enter after
each: `Nina`, `Luka`, `Nina`, `Ana`, `done`.

Expected output, as it looks in the terminal (the lines `Nina`,
`Luka`, `Nina`, `Ana` and `done` are what you typed):
```
Vote (or done):
Nina
Vote (or done):
Luka
Vote (or done):
Nina
Vote (or done):
Ana
Vote (or done):
done
Nina: 2
Luka: 1
Ana: 1
Winner: Nina
```

Run it a second time and type only `done`. Expected output:
```
Vote (or done):
done
No votes.
```
