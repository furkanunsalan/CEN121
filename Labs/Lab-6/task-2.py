def my_solution():
    set_1 = set()
    set_2 = set()

    first_file = open(input("Enter the name of the first file: "))
    second_file = open(input("Enter the name of the second file: "))

    for word in first_file.read().split():
        set_1.add(word)

    for word in second_file.read().split():
        set_2.add(word)

    first_file.close()
    second_file.close()

    unique_words = set_1.union(set_2) # Birleşim
    intersection = set_1.intersection(set_2) # Kesişim
    in_first = set_1.difference(set_2) # set_1'de olup set_2'de olmayanlar
    in_second = set_2.difference(set_1) # set_2'de olup set_1'de olmayanlar
    sym_diff = set_1.symmetric_difference(set_2) # set_1 ve set_2'de olup ikisinin de ortak olarak bulunmayanlar

    print()
    print("Unique words: ", unique_words, "\n")
    print("Intersection: ", intersection, "\n")
    print("Words in first file but not in second file: ", in_first, "\n")
    print("Words in second file but not in first file: ", in_second, "\n")
    print("Words that appear in any of the files but not in both: ", sym_diff, "\n")

my_solution()