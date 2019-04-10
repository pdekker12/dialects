import pandas as pd
DATA_FILE_TSV = "data/union_table.tsv"
df = pd.read_csv(DATA_FILE_TSV, sep="\t")
print(df)