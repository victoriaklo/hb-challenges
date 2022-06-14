def split(astring, splitter):
    """Split a string by splitter and return list of splits.
    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']
    """
    result = []
    # keep track of current index
    idx = 0

    while idx <= len(astring):
        curr_idx = idx
        idx = astring.find(splitter, idx)

        if idx != -1:
            result.append(astring[curr_idx : idx])
            idx += len(splitter)
        
        else:
            result.append(astring[curr_idx:])
            break
    
    return result

    
print(split("i love balloonicorn", " "))
print(split("that is which is that which is that", " that "))
print(split("that is which is that which is that", "that"))
print(split("hello world", "nope"))
    