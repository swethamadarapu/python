def count_letters_in_words(input_string):

    words = input_string.split()
    word_counts = {}
    for word in words:
        count = 0
        for char in word:
            if char.isalpha():
                count += 1
        word_counts[word] = count
    
    return word_counts

input_string = "this is swetha madarapu"
result = count_letters_in_words(input_string)
for word, count in result.items():
    print(f"{word}: {count}")

