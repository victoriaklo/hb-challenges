def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name.
    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'
    """

    # first split the word by underscore
    # uppercase each first letter in word
    # join at the end
 
    words = variable_name.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    return "".join(words)

