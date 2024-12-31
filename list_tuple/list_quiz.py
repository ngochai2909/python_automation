def pig_latin(text):
    # Separate the text into words
    words = text.split()
    pig_latin_words = []

    for word in words:
        # Create the pig latin word and add it to the list
        new_word = word[1:] + word[:1] + "ay"
        pig_latin_words.append(new_word)

    # Join the words back into a phrase
    return " ".join(pig_latin_words)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"