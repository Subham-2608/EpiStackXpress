import pandas as pd
from functools import reduce

# ──────────────────────────────────────────────────────────────────────────────
# BS-Seq file name map
# ──────────────────────────────────────────────────────────────────────────────
_REGION_FILES = [
    ("CDS",      "CDS_Positive_methylation_counts.csv",            "CDS_Negative_methylation_counts.csv"),
    ("Intron",   "intron_Positive_methylation_counts.csv",         "intron_Negative_methylation_counts.csv"),
    ("Promoter", "Promoter_Positive_methylation_counts.csv",       "Promoter_Negative_methylation_counts.csv"),
    ("Five",     "Five_prime_UTR_Positive_methylation_counts.csv", "Five_prime_UTR_Negative_methylation_counts.csv"),
    ("Three",    "Three_prime_UTR_Positive_methylation_counts.csv","Three_prime_UTR_Negative_methylation_counts.csv"),
]
_REGIONS   = [r[0] for r in _REGION_FILES]
_CONTEXTS  = ["CpG", "CHG", "CHH"]
_DROP_COLS = ["ID", "Source", "Portion", "Start", "End", "score", "Strand", "Phase"]


def _clean_df(df, region):
    """Drop metadata columns and rename count columns to include region label."""
    df = df.drop(columns=[c for c in _DROP_COLS if c in df.columns])
    rename = {}
    for ctx in _CONTEXTS:
        rename[f"{ctx}_OT_Count"] = f"{ctx}_{region}_Count"
        rename[f"{ctx}_OB_Count"] = f"{ctx}_{region}_Count"
    return df.rename(columns=rename)


def _normalize_counts(df):
    """Divide each context-region count by the region length, then drop length cols."""
    df = df.copy()
    for region in _REGIONS:
        for ctx in _CONTEXTS:
            col = f"{ctx}_{region}_Count"
            if col in df.columns:
                df[col] = df[col] / df[f"{region}_length"]
    return df.drop(columns=[f"{r}_length" for r in _REGIONS], errors="ignore")


def load_BSseq(bs_folder):
    
    import os

    pos_dfs, neg_dfs = [], []

    for region, pos_file, neg_file in _REGION_FILES:
        for fname, store in [(pos_file, pos_dfs), (neg_file, neg_dfs)]:
            df = pd.read_csv(os.path.join(bs_folder, fname))
            df = _clean_df(df, region)
            df = df[df["length"].notna() & (df["length"] > 0)]
            df = df.groupby("Reference_id", as_index=False).sum(numeric_only=True)
            df = df.rename(columns={"length": f"{region}_length"})
            store.append(df)

    merge = lambda dfs: reduce(
        lambda l, r: pd.merge(l, r, on="Reference_id", how="inner"), dfs
    )

    merged = pd.concat(
        [_normalize_counts(merge(pos_dfs)),
         _normalize_counts(merge(neg_dfs))],
        axis=0,
        ignore_index=True
    )

    return merged.reset_index(drop=True)