def solve(in_order, out_order):
    '''(list of int, list of int) -> int

    Returns an integer code (0 = none, 1 = stack only, 2 = queue only, 3 = both)
    whether a given list is a stack, a queue, both, or neither. 

    >>> solve([], [])
    3
    >>> solve([1, 2, 3, 4], [1, 2, 3, 4])
    2
    >>> solve([1, 2, 3, 4], [4, 3, 2, 1])
    1
    >>> solve([1, 2, 2, 1], [1, 2, 2, 1])
    3
    >>> solve([1, 2, 3, 4], [2, 3, 1, 4])
    0
    '''
    stack = True
    queue = True

    for index in range(len(in_order)):
        if in_order[index] != out_order[index]:
            queue = False
        if in_order[index] != out_order[-1 - index]:
            stack = False

    if queue and stack:
        return 3
    elif queue and not stack:
        return 2
    elif not queue and stack:
        return 1
    return 0
