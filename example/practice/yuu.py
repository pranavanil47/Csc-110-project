def list_even_lengths(string):
    word_count = []
    word_list = string.split()
    for word in word_list:
        if len(word) % 2 == 0:
            if word not in word_count:
                word_count.append(word)
                word_count.append(0)
            index = word_count.index(word)
            word_count[index + 1] += 1
        for i in range(0,len(word_count) - 1, 2):
            print(word_count[i], ":", word_count[i + 1])

list_even_lengths('Hello, how are you? Hello, I am doing well. I am too!')