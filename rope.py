class Rope(object):

    def __init__(self, data=''):
        self.length = len(data)
        self.left = None
        self.right = None
        self.data = data

    def __add__(self, other):
        r = Rope()
        r.left = self
        r.right = other
        r.length = self.length + other.length
        return r

    def __getitem__(self, index):
        # TODO: Combine int and slice?
        #       Or is it faster to separate them?

        if isinstance(index, int):
            # NOTE: It should not be necessary to check both
            if self.left and self.right:
                if index < self.left.length:
                    return self.left[index]
                else:
                    return self.right[index - self.left.length]
            else:
                return Rope(self.data[index])

        elif isinstance(index, slice):
            i, j = index.start, index.stop

            if self.left and self.right:
                if not i or i < self.left.length:
                    if j and j <= self.left.length:
                        return self.left[i:j]
                    else:
                        rj = j - self.left.length if j else None
                        return self.left[i:] + self.right[:rj]
                else:
                    rj = j - self.left.length if j else None
                    return self.right[(i - self.left.length):rj]
            else:
                if (not i) and (not j or j == self.length):
                    return self
                else:
                    return Rope(self.data[i:j])

        else:
            raise TypeError('list indices must be integers or slices, not {}'
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

    # API
    def reduce(self):
        """Search the tree and remove any redundant nodes."""
        raise NotImplementedError

    def insert(self, index, s):
        """Insert string s at index i."""
        raise NotImplementedError
