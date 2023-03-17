from bionumpy.bnpdataclass import bnpdataclass


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
