"""Main module."""
from bionumpy.bnpdataclass import bnpdataclass
import bionumpy as bnp
import dataclasses
from .atom import Atom


def parse_file(file_obj):
    atom_lines = (line.strip() for line in file_obj if line.startswith('ATOM'))
    types = [field.type for field in dataclasses.fields(Atom)]
    args = zip(*((t(p) for t, p in zip(types, line.split()[1:12])) for line in atom_lines))
    return Atom(*[list(a) for a in args])


def read(filename):
    with open(filename) as f:
        return parse_file(f)


class PDB:
    ''' Class to hold data from a PDB file '''
    def __init__(self, atoms: Atom):
        self._chains = dict(bnp.groupby(atoms, 'chain'))

    @property
    def chains(self) -> dict[str, Atom]:
        """Dict containing the atoms of each chain in the pdb file

        Returns
        -------
        dict[str, Atom]
        """
        return self._chains

    @classmethod
    def from_atoms(cls, atoms: Atom) -> 'PDB':
        """Create a PDB object from a set of atoms

        Parameters
        ----------
        atoms : Atom

        Returns
        -------
        'PDB'
        """
        
        return cls(atoms)

    @classmethod
    def from_file(cls, filename: str) -> 'PDB':
        """Create a PDB object from a pdb file

        Parameters
        ----------
        cls :
        filename : str

        Returns
        -------
        'PDB'
        """
        
        return cls.from_atoms(read(filename))
