import numpy as np
import pandas as pd
import sys, datetime
import goenrich
import scipy.stats as stat

def main():
    df = pd.read_csv('goa_human.gaf', sep='`', skiprows=41, header=None)
    matrix = np.chararray((df.shape[0], 17), itemsize=150, unicode=True)

    for i, row in enumerate(df.itertuples()):
        progressPercent = ((i + 1) / len(df.index)) * 100

        sys.stdout.write("Progress: %d%%  %d Out of %d   \r" % (progressPercent, (i + 1), len(df.index)))
        sys.stdout.flush()

        lst = row[1].split('\t')

        matrix[i, :] = lst

    df_clean = pd.DataFrame(data=matrix)
    columns = ["DB", "DB gene ID", "Gene symbol", "Qualifier", "GO ID", "Reference", "Evidence code", "Evidence from",
               "GO class", "attribute", "Locus tag", "gene/protein", "tax id", "date", "Assigned by",
               "additional information", "empty"]
    df_clean.columns = columns

    df_component = df_clean[df_clean["GO class"] == 'C'].copy()

