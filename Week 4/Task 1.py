import string
import os
with open(r"C:\Users\mansu\OneDrive\Рабочий стол\Week 4\text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
line_count = len(lines)
word_count = 0
words_freq = {}

for line in lines:
    line = line.lower()
    line = line.translate(str.maketrans("","",string.punctuation))
    words = line.split()
    word_count += len(words)

    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1

with open("analysis.txt", "w", encoding="utf-8") as file:
    file.write(f"Total lines: {line_count}\n")
    file.write(f"Total words: {word_count}\n")
    file.write("Word frequency:\n")
    for word, count in words_freq.items():
        file.write(f"{word}: {count}\n")

