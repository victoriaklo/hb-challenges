def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
	# split the input phrase into a list by space
    # iterate through the list, have a conditional if the index at 0 is a vowel + 'yay' at the end
    # else, word[1:] + word[0] + 'ay'
    # return ' '.join(words)
    words = phrase.split(' ')
    pig_latin_phrase = []
    for word in words:
        if word[0] in 'aeiou':
            pig_latin = word + 'yay'
            pig_latin_phrase.append(pig_latin)
        else:
            pig_latin = word[1:] + word[0] + 'ay'
            pig_latin_phrase.append(pig_latin)

    return ' '.join(pig_latin_phrase)
            
print(pig_latin('hello awesome programmer'))