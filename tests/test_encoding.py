from bnp_pdb.encodings import AtomEncoding
import bionumpy as bnp


def test_atom_encoding():
    bnp.as_encoded_array(['N', 'NE'], AtomEncoding)


def test_atom_encoding():
    bnp.as_encoded_array('NE', AtomEncoding)
