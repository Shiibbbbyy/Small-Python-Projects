class Stack:

    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self: 'Stack') -> None:
        '''A new empty Stack.'''
        self._data = []

    def pop(self: 'Stack') -> object:
        '''Remove and return the top item.

        >>> s = Stack()
        >>> s.push(2)
        >>> s.push(3)
        >>> s.pop()
        3
        '''
        return self._data.pop()

    def is_empty(self: 'Stack') -> bool:
        '''Return whether the stack is empty.

        >>> s = Stack()
        >>> s.push(4)
        >>> s.pop()
        4
        >>>s.is_empty()
        True
        '''
        return self._data == []

    def push(self: 'Stack', o: object) -> None:
        '''Place o on top of the stack.'''
        self._data.append(o)

    def peek(self: 'Stack') -> object:
        '''Return the top item without removing it.

        >>> s = Stack()
        >>> s.push(2)
        >>> s.push(3)
        >>> s.peek()
        3
        '''
        return self._data[-1]

    def size(self: 'Stack') -> int:
        '''Return the number of elements on the stack.

        >>> s = Stack()
        >>> s.push(2)
        >>> s.push(3)
        >>> s.size()
        2
        '''
        return len(self._data)


def solve(lst):
    '''(list of int) -> int

    Returns the max number of elements that can be sorted in a list using a
    maximum of 1 stack.

    >>> solve([])
    0
    >>> solve([5, 4, 3, 2, 1])
    5
    >>> solve([4, 5, 2, 1, 3])
    3
    >>> solve([1, 2, 3, 4, 5])
    5
    '''
    num_stack = Stack()
    index = 0
    current = 0

    while len(lst) > index:
        if lst[index] == current + 1:
            current += 1
            index += 1
        else:
            num_stack.push(lst[index])
            index += 1
        while num_stack.size() > 0 and num_stack.peek() == current + 1:
            num_stack.pop()
            current += 1
    return current
