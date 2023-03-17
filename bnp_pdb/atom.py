from bionumpy.bnpdataclass import bnpdataclass
from .encodings import AtomEncoding, ResidueEncoding

@bnpdataclass
class Atom:
    atom_number: int
    atom: AtomEncoding
    residue: ResidueEncoding
    chain: str
    residue_number: int
    x: float
    y: float
    z: float
    occupancy: float
    temperature_factor: float
    element_name: str
