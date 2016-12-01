import math


class Distance(object):
    @classmethod
    def vector_substract(cls, v, w):
        return [i - j for i, j in zip(v, w)]

    @classmethod
    def dot(cls, v, w):
        return sum(i * j for i, j in zip(v, w))

    @classmethod
    def sum_of_squares(cls, v):
        return cls.dot(v, v)

    @classmethod
    def magnitude(cls, v):
        return math.sqrt(cls.sum_of_squares(v))

    @classmethod
    def distance(cls, v, w):
        return cls.magnitude(cls.vector_substract(v, w))
