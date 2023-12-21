def solution():
    file = open("Assignments/Assignment-5/text.txt", "r")
    words = file.read().split()
    file.close()
    words_set = set(words)
    print(words_set)

solution()