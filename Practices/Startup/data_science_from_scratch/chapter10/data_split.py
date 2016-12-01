import random


def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)

    return results


def train_test_split(x, y, test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)

    return x_train, x_test, y_train, y_test


if __name__ == '__main__':
    xx_train, xx_test, yy_train, yy_test = train_test_split([[1, 2], [3, 1], [2, 3], [4, 1]], [0, 1, 0, 1], 0.5)
    print(xx_test)
