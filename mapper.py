import sys

# Mapper will read input line by line
for line in sys.stdin:
    # Remove any extra whitespace and split line into words
    words = line.strip().split()
    
    # For each word, output the word and the count (1)
    for word in words:
        print(f"{word.lower()}\t1")
