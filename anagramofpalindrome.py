# Is the word an anagram of a palindrome?

# A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).

# Determine if the given word is a re-scrambling of a palindrome.

# The word will only contain lowercase letters, a-z.

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    
    """
    if len(word) == 1:
        return True
    
    # create a dictionary of char as key and count as the value
    # a palindrome has even nums of chars and 1 char that can be 1.
    # check if the word has 1 char that has count 1

    # pseudocode:
    # create an empty dictionary
    # create a count variable 

    # iterate through all char in word, and add it to dictionary
    # set count to value of the key char and increment count when the char is seen

    # check if the chars dict has a character with count 1 or 0, if yes, then its a palendrome

    chars_dict = {}
    count = 0

    for char in word:
        # use get so you do not run into an error
        count = chars_dict.get(char, 0)
        chars_dict[char] = count + 1
    
    # set the seen_odd_char to False
    seen_odd_char = False

    for count in chars_dict.values():
        if count % 2 != 0:
            if seen_odd_char:
                return False
            
            seen_odd_char =True
    
    return True