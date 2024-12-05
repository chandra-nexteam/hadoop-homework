import sys

current_word = None
current_count = 0

# Read input line by line
for line in sys.stdin:
    # Strip leading/trailing whitespaces and split by tab
    word, count = line.strip().split('\t')
    
    # Convert count to integer
    count = int(count)
    
    # If the word is the same as the last word, accumulate the count
    if word == current_word:
        current_count += count
    else:
        # If we have a new word, output the old word and its count
        if current_word:
            print(f"{current_word}\t{current_count}")
        
        # Set the current word to the new word and its count to the current count
        current_word = word
        current_count = count

# Don't forget to output the last word and its count
if current_word:
    print(f"{current_word}\t{current_count}")
