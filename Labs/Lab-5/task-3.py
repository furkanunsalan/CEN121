def frequency():
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0]
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    frequent = 0

    user_string = input("Enter a string: ")
    for ch in user_string.upper():
        ch = ch.upper()

        index = letter.find(ch)
        if index >= 0:
            count[index] += 1
    
    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i
    
    print("The most frequent letter is", letter[frequent], "with a count of", count[frequent])


frequency()