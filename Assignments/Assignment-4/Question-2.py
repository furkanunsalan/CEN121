def solution():
    A = ("cat", "bird", "dolphin", "giraffe", "elephant", "dog")
    
    longest_word = ""
    longest_length = 0
    
    for word in A:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word

    print(f"{longest_word} is the longest word in the tuple A. It's length is {longest_length}.")

solution()