import bnp_pdb
import bionumpy as bnp
from itertools import combinations
import plotly.express as px
import plotly.graph_objects as go


def plot_bars(**counter_dict):
    fig = go.Figure()
    for name, counter in counter_dict.items():
        fig.add_trace(go.Bar(x=counter.alphabet,
                             y=counter.proportions,
                             name=name))
    return fig


pdb = bnp_pdb.PDB.from_file('/home/knut/Downloads/1n8z.pdb')
A, C = pdb.chains['A'], pdb.chains['C']
A = A[(A.atom == 'CA') | (A.atom == 'CB')]
C = C[(C.atom == 'CA') | (C.atom == 'CB')]
table = bnp_pdb.distance_table(A, C)
all_a_count = bnp.count_encoded(table.atom_a.residue)
all_b_count = bnp.count_encoded(table.atom_b.residue)
px.histogram(table.distance).write_image('docs_source/figures/distance_hist.png')
table = table[table.distance < 30]
close_a_count = bnp.count_encoded(table.atom_a.residue)
close_b_count = bnp.count_encoded(table.atom_b.residue)
plot_bars(all_counts_A=all_a_count, close_count_A=close_a_count).write_image('docs_source/figures/residue_proportions_a.png')
plot_bars(all_counts_C=all_b_count, close_count_C=close_b_count).write_image('docs_source/figures/residue_proportions_c.png')


# for chain_name_a, chain_name_b in combinations(pdb.chains.keys(), 2):
#     A, B = pdb.chains[chain_name_a], pdb.chains[chain_name_b]
#     A = A[(A.atom == 'CA') | (A.atom == 'CB')]
#     B = B[(B.atom == 'CA') | (B.atom == 'CB')]
#     table = bnp_pdb.distance_table(A, B)
#     px.histogram(table.distance).show()
    # all_a_count = bnp.count_encoded(table.atom_a.residue)
    # all_b_count = bnp.count_encoded(table.atom_b.residue)
    # table = table[table.distance < 10]
    # close_a_count = bnp.count_encoded(table.atom_a.residue)
    # close_b_count = bnp.count_encoded(table.atom_b.residue)
    # plot_bars(all_counts=all_a_count, close_count=close_a_count).show()
    # plot_bars(all_counts=all_b_count, close_count=close_b_count).show()
    #print(table)
    # print(table.atom_a)
    # matrix = bnp_pdb.distance_matrix(pdb.chains[chain_name_a],
    #                                  pdb.chains[chain_name_b])
    # labels = dict(x=chain_name_a, y=chain_name_b, color="Distance")
    # print(labels)
    # print(matrix)
    # fig = px.imshow(matrix).show()
