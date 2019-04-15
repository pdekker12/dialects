import os
import pandas as pd
from lingpy.align.sca import Alignments
import html
import re

DATA_TSV = "data/union_table_wld.tsv"
DATA_LINGPY_TSV = DATA_TSV.split(".")[0] + "_lingpy.tsv"
TYPE = "wld"
COLS = ["dictionary", "publication_id", "lemma", "keyword", "lexical_variant", "phonetic_variant", "definition", "definition_question", "publish", "lemma_comment", "keyword_comment", "dialect_form_comment", "lemma_id", "definition_sourcebook", "definition_sourcebook_pages", "definition_sourcelist", "question_id", "context_comment", "location_kloeke", "location_comment", "location_place", "location_area", "location_subarea", "respondent_id", "context_link_to_scan", "record_id"]

# Read in original csv, restrict columns, and rename columns to LingPy format
df = pd.read_csv(DATA_TSV, sep="\t", header=None, names=COLS)
df["phonetic_peter"] = df["phonetic_variant"].map(html.unescape)
df = df.rename(columns={"lemma": "concept", "location_place":"doculect", "phonetic_peter":"ipa" })
# Remove parts between brackets
df["ipa"] = df["ipa"].map(lambda s: re.sub(r"\s*\(.+\)", "", s))
df["cogid"]= "1"
df = df[["concept", "doculect", "ipa", "cogid"]]

df.to_csv(DATA_LINGPY_TSV, sep="\t", index_label="id")

# Load data into LingPy
#al = Alignments(DATA_LINGPY_TSV)
# Multiple-sequence alignment using SCA model
#al.align(model="asjp")