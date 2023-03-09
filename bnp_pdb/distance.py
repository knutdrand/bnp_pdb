import numpy as np


def euclidian_distance(point_a, point_b):
    return np.sqrt((point_a.x-point_b.x)**2,
                   (point_a.y-point_b.y)**2,
                   (point_a.z-point_b.z)**2)


def distance_matrix(point_a, point_b):
    return np.sqrt((point_a.x-point_b.x[:, None])**2 +
                   (point_a.y-point_b.y[:, None])**2 +
                   (point_a.z-point_b.z[:, None])**2)
