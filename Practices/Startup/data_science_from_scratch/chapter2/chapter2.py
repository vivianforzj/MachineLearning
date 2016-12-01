from collections import defaultdict

document = ["as", "hello", "as", "I", "world"]

word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list["t"].append("yes")

dd_dict = defaultdict(dict)
dd_dict["hah"]["city"] = "Shanghai"

from collections import Counter

c = Counter([0, 3, 1, 1])

word_counts = Counter(document)
for word, count in word_counts.most_common(10):
    print(word, count)

import re

a1 = re.match("cat", "cat")
a2 = re.search("at", "cat")
a3 = re.sub("[0-9]", "-", "R2D2")

print(re.split("[ab]", "cagrgbll"))

from functools import partial


def exp(base, power):
    return base ** power


two_to_the = partial(exp, 2)
print(two_to_the(3))

square_of = partial(exp, power=2)
print(square_of(3))


def double(x):
    return 2 * x


xs = [1, 2, 3, 4]
twice_xs = map(double, xs) # same as abov

list_doubler = partial(map, double) # *function* that doubles a list
twice_xs_partial = list_doubler(xs) # again [2, 4, 6, 8]
