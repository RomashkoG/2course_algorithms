import string

n, m = map(int, input().split())

dictionary = set()

for i in range(n):
    word = input().strip().lower()
    dictionary.add(word)

text_words = set()

for i in range(m):
    line = input().strip().lower()

    for ch in string.punctuation:
        line = line.replace(ch, ' ')
    words = line.split()
    for word in words:
        text_words.add(word)

if all(word in dictionary for word in text_words) and all(word in text_words for word in dictionary):
    print("Everything is going to be OK.")
elif not all(word in dictionary for word in text_words):
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")