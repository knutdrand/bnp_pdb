"""Console script for bnp_pdb."""
from .bnp_pdb  import PDB
from .distance import distance_matrix
# todo


import typer


def distances(filename: str):
    '''
    Simple function

    >>> main()

    '''
    pdb = PDB.from_file(filename)
    chain_names = list(pdb.chains.keys())
    for chain_a in chain_names[:-1]:
        for chain_b in chain_names[1:]:
            print(chain_a, chain_b)
            matrix = distance_matrix(pdb.chains[chain_a], pdb.chains[chain_b])
            print(matrix)


def main():
    typer.run(distances)


if __name__ == "__main__":
    main()
