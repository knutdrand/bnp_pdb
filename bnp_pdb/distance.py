import numpy as np
from bionumpy.bnpdataclass import bnpdataclass
from .atom import Atom


@bnpdataclass
class AtomDistance:
    atom_a: Atom
    atom_b: Atom
    distance: float


def euclidian_distance(point_a, point_b):
    return np.sqrt((point_a.x-point_b.x)**2 +
                   (point_a.y-point_b.y)**2 +
                   (point_a.z-point_b.z)**2)


def distance_matrix(point_a, point_b):
    return np.sqrt((point_a.x-point_b.x[:, None])**2 +
                   (point_a.y-point_b.y[:, None])**2 +
                   (point_a.z-point_b.z[:, None])**2)


def distance_table(atom_a: Atom, atom_b: Atom):
    x_idx, y_idx = np.mgrid[0:len(atom_a), 0:len(atom_b)]
    a = atom_a[x_idx.ravel()]
    b = atom_b[y_idx.ravel()]
    distances = distance_matrix(atom_a, atom_b).ravel()
    return AtomDistance(a, b, distances)
