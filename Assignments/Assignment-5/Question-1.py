def solution():
    file = open("Assignments/Assignment-5/text.txt", "r")
    words = file.read().split()
    file.close()
    words_set = set(words)
    print("Here are the unique words in the file:")
    for word in words_set:
        print(word)

solution()
