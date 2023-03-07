"""Main module."""
from bionumpy.bnpdataclass import bnpdataclass
import bionumpy as bnp
import dataclasses

@bnpdataclass
class Atom:
    atom_number: int
    atom: str
    residue: str
    chain: str
    residue_number: int
    x: float
    y: float
    z: float
    occupancy: float
    temperature_factor: float
    element_name: str


def parse_file(file_obj):
    atom_lines = (line.strip() for line in file_obj if line.startswith('ATOM'))
    types = [field.type for field in dataclasses.fields(Atom)]
    args = zip(*((t(p) for t, p in zip(types, line.split()[1:12])) for line in atom_lines))
    return Atom(*[list(a) for a in args])


def read(filename):
    with open(filename) as f:
        return parse_file(f)


class PDB:
    def __init__(self, atoms: Atom):
        self._chains = dict(bnp.groupby(atoms, 'chain'))

    @property
    def chains(self) -> dict[str, Atom]:
        return self._chains

    @classmethod
    def from_atoms(cls, atoms: Atom):
        return cls(atoms)

    @classmethod
    def from_file(cls, filename: str):
        return cls.from_atoms(read(filename))
