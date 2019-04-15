import os
import pandas as pd
from lingpy.align.sca import Alignments

DATA_TSV = "data/union_table.tsv"
DATA_LINGPY_TSV = "data/union_table_lingpy.tsv"

if not os.path.exists(DATA_LINGPY_TSV):
    # Read in original csv, restrict columns, and rename columns to LingPy format
    df = pd.read_csv(DATA_TSV, sep="\t")
    df = df[["lemma_id", "location_kloeke","phonetic"]]
    df = df.rename(columns={"lemma_id": "concept", "location_kloeke":"doculect", "phonetic":"ipa" })
    df["cogid"]= "1"
    df.to_csv(DATA_LINGPY_TSV, sep="\t", index_label="ID")

# Load data into LingPy
al = Alignments(DATA_LINGPY_TSV)

# Multiple-sequence alignment using SCA model
al.align(model="asjp")