def solution():
    sentence = input("Enter a sentence: ")
    splitted_sentence = sentence.split(" ")
    NEW_SENTENCE = ""
    for item in splitted_sentence:
        first = item[0]
        removed = item.replace(item[0], "", 1)
        added = removed + first + "ay "
        NEW_SENTENCE += added
    print(NEW_SENTENCE.upper())

solution()