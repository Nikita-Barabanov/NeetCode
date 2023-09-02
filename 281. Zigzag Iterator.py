from itertools import zip_longest


class ZigzagIterator(object):

    def __init__(self, *vs):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.val = (elem for z in zip_longest(*vs) for elem in z if elem)
        self.n = sum(map(len, vs))

    def next(self):
        """
        :rtype: int
        """
        self.n -= 1
        return next(self.val)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
v1 = [1,2,3]
v2 = [4,5,6,7]
v3 = [8,9]
z = ZigzagIterator(v1, v2, v3)
while z.hasNext():
    print(z.next())

