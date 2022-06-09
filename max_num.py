def max_num(num_list):
    """Returns largest integer from given list
    >>> max_num([5, 3, 6, 2, 1])
    6
    """
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num
    
    return max