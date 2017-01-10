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
        if self.left and self.right:    # Checking both is redundant...
            if index < self.left.length:
                return self.left[index]
            else:
                return self.right[index - self.left.length]
        else:
            return self.data[index]

    def get_string(self):
        s = ''
        if self.left and self.right:
            s = self.left.get_string() + self.right.get_string()
        else:
            s = self.data
        return s

    @property
    def word(self):
        return self.get_string()
