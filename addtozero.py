# Given the wording of our problem, a zero in the list will always make this true, 
# since “any two numbers” could include that same zero for both numbers, and they sum to zero:


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.
        >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True"""

    #pseudocode:

    # which data structures will help us with this?

    # use a hashmap or something else to store all the elements in the list ? set? because look up time is also constant
    # then compare if the opposite of n/-n is present in the map

    # create an empty set to track the items in the list that we've seen already
    # iterate through the nums list and add each item to set
        # check if the opposite of n is in the nums list
        # if it is, return True else return False


