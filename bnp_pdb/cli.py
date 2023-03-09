"""Console script for bnp_pdb."""
from itertools import combinations
import plotly.express as px
import bnp_pdb

# todo


import typer


def distances(filename: str, out_filename: str = None):
    '''
    Simple function

    >>> main()

    '''
    pdb = bnp_pdb.PDB.from_file(filename)
    for chain_a, chain_b in combinations(pdb.chains.keys(), 2):
        matrix = bnp_pdb.distance_matrix(pdb.chains[chain_a], pdb.chains[chain_b])
        fig = px.imshow(
            matrix,
            labels=dict(x=chain_a, y=chain_b, color="Distance"))
        if out_filename is not None:
            fig.write_image(out_filename)
        else:
            fig.show()


def main():
    typer.run(distances)


if __name__ == "__main__":
    main()
