import random

from numpy import mean

from data_science_from_scratch.util.distance import Distance


def random_point(dim):
    return [random.random() for _ in range(dim)]


def random_distances(dim, num_pairs):
    return [Distance.distance(random_point(dim), random_point(dim)) for _ in range(num_pairs)]


if __name__ == '__main__':
    dimensions = range(1, 101, 5)

    avg_distances = []
    min_distances = []

    random.seed(0)
    for dim in dimensions:
        distances = random_distances(dim, 10000)  # 10,000 random pairs
        avg_distances.append(mean(distances))  # track the average
        min_distances.append(min(distances))  # track the minimum
        print(dim, min(distances), mean(distances), min(distances) / mean(distances))