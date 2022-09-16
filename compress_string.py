# Write a function that takes in a string and returns a compressed version of that string. Your string will only contain non-numeric characters — that is, it will only contain letters, whitespace, and punctuation.
# 'Hello, world! Cows go moooo...' => 'Hel2o, world! Cows go mo4.3'

# 'balloonicorn' => 'bal2o2nicorn'


def compress(string):
    """Return a compressed version of the given string."""

    compressed = []

    current = ''
    count = 0
    for ch in string:
        if ch != current:
            compressed.append(current)
            # Only append count if it is greater than 1
            if count > 1:
                compressed.append(str(int(count)))

            # Reset `count` and update `current`
            current = ch
            count = 0

        count += 1

    # Append remaining character(s)
    compressed.append(current)
    if count > 1:
        compressed.append(str(int(count)))

    return ''.join(compressed)
