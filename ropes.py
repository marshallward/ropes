__version__ = '0.0.1'

class Rope(object):
    # NOTE: self.left and self.right should either both point to subnodes or
    #       both set to `None`, so checking both should not be necessary.

    def __init__(self, data=''):
        if isinstance(data, list):
            if len(data) == 0:
                self.__init__()
            elif len(data) == 1:
                self.__init__(data[0])
            else:
                # Round-up division (to match rope arithmetic associativity)
                idiv = len(data) // 2 + (len(data) % 2 > 0)

                self.left = Rope(data[:idiv])
                self.right = Rope(data[idiv:])
                self.data = ''
                self.length = self.left.length + self.right.length
        elif isinstance(data, str):
            self.left = None
            self.right = None
            self.data = data
            self.length = len(data)
        else:
            raise TypeError('Only strings are currently supported')

        # Word iteration
        self.current = self

    def __eq__(self, other):
        if (self.left and self.right) and (other.left and other.right):
            return self.left == other.left and self.right == other.right
        elif (self.left and self.right) or (other.left and other.right):
            return False
        else:
            return self.data == other.data

    def __add__(self, other):
        # TODO: Automatically collapse empty ropes
        r = Rope()
        r.left = self
        r.right = other
        r.length = self.length + other.length
        r.current = self
        return r

    def __getitem__(self, index):

        if isinstance(index, int):
            if index < 0:
                index += self.length

            if index < 0 or index >= self.length:
                raise IndexError('rope index out of range')

            if self.left and self.right:
                if index < self.left.length:
                    return self.left[index]
                else:
                    return self.right[index - self.left.length]
            else:
                return Rope(self.data[index])

        elif isinstance(index, slice):
            # Normalise the indexes
            i = index.start if index.start is not None else 0
            j = index.stop if index.stop is not None else self.length

            if i < 0:
                i += self.length
            if j < 0:
                j += self.length

            i = min(max(i, 0), self.length)
            j = min(max(j, 0), self.length)

            if self.left and self.right:
                if i < self.left.length:
                    if j <= self.left.length:
                        return self.left[i:j]
                    else:
                        return (self.left[i:]
                                + self.right[:(j - self.left.length)])
                else:
                    return self.right[(i - self.left.length)
                                      :(j - self.left.length)]
            else:
                if i <= 0 and j >= self.length:
                    return self
                else:
                    return Rope(self.data[i:j])

        else:
            raise TypeError('rope indices must be integers or slices, not {}'
                            ''.format(type(index).__name__))

    def __repr__(self):
        # TODO: Parentheses are too conservative, need to clean this up
        if self.left and self.right:
            return '{}{} + {}{}'.format('(' if self.left else '',
                                        self.left.__repr__(),
                                        self.right.__repr__(),
                                        ')' if self.right else '')
        else:
            return "Rope('{}')".format(self.data)

    def __str__(self):
        if self.left and self.right:
            return self.left.__str__() + self.right.__str__()
        else:
            return self.data

    def __iter__(self):
        return self

    def __next__(self):
        if self.current:
            if self.left and self.right:
                try:
                    return next(self.left)
                except StopIteration:
                    self.current = self.right
                return next(self.right)
            else:
                self.current = None
                return self.data
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

    # API
    def reduce(self):
        """Search the tree and remove any redundant nodes."""
        raise NotImplementedError

    def insert(self, index, s):
        """Insert string s at index i."""
        raise NotImplementedError
