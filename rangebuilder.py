#
# This is an example of how to write a chain API.
# This is an important skill when designing DSL (https://en.wikipedia.org/wiki/Domain-specific_language)
#

class RangeBuilder(object):

    def __init__(self):
        self.start = 0
        self.end = 0
        self.range_step = 1
        self.include_last = False
        self.reversed = False

    def from_(self, start): # from cannot be used as a method name since it is a keyword in Python
        self.start = start
        return self

    def to(self, end):
        self.end = end
        return self

    def withLast(self):
        self.include_last = True
        return self

    def step(self, step):
        self.range_step = step
        return self

    def reverse(self):
        self.reversed = not self.reversed
        return self

    def __iter__(self):
        if not self.reversed:
            start = self.start
            end = self.end
            step = self.range_step
            if self.include_last:
                end += 1
        else:
            start = self.end
            end = self.start
            step = -self.range_step
            if self.include_last:
                end -= 1

        return iter(range(start, end, step))



if __name__ == '__main__':
    for i in RangeBuilder().from_(0).to(6).withLast().reverse():
        print(i)