def fit_to_width(str, limit):
    """
    >>> fit_to_width('Hello, world! I love Python and Hackbright',
    ...              10)
    Hello,
    world! I
    love
    Python and
    Hackbright
    """
    words = str.split()
    lines = []

    curr_line = []
    for word in words:
        if len(' '.join(curr_line + [word])) <= limit:
            curr_line.append(word)
        else:
            if curr_line:
                lines.append(' '.join(curr_line))
            curr_line = []
    

    lines.append(' '.join(curr_line))

    for line in lines:
        print(line)

def fit_to_width(string, limit):
    """Print string within a character limit."""

    # START SOLUTION

    # Create a stack of tokens
    tokens = list(reversed(string.split()))
    lines = []

    curr_line = []
    while tokens:
        # Test to see if current word fits in the line
        word = tokens[-1]
        if len(' '.join(curr_line + [word])) <= limit:
            curr_line.append(tokens.pop())

        # If the word doesn't fit, start a new line
        else:
            if curr_line:
                lines.append(' '.join(curr_line))
            curr_line = []

    # Append remaining line
    lines.append(' '.join(curr_line))

    for line in lines:
        print(line)