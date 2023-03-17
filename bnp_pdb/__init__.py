"""Top-level package for BioNumPy PDB."""

__author__ = """Knut Rand"""
__email__ = 'knutdrand@gmail.com'
__version__ = '0.0.1'

from .bnp_pdb import PDB
from .distance import distance_matrix, distance_table
__all__ = ['PDB', 'distance_matrix']
