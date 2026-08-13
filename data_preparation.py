"""
Stage 1: Data preparation.

Reshapes the OHID Fingertips extract from long indicator format into a
modelling dataset. Each row is one population subgroup in one survey year,
carrying its physical activity, obesity and diet indicators side by side.

"""

from pathlib import Path

import numpy as np
import pandas as pd

RAW = Path("data/raw/indicator-data.csv")
OUT = Path("data/processed/analysis_dataset.csv")

INDICATORS = {
    93014: "pct_active",
    93015: "pct_inactive",
    93088: "pct_overweight_obese",
    93881: "pct_obese",
    93982: "pct_5aday",
}

DIMENSIONS = {
    "Ethnic groups": "Ethnicity",
    "Disability": "Disability",
    "LSOA11 deprivation deciles within area (IMD  trend)": "Deprivation",
    "Socioeconomic class": "Socioeconomic class",
    "Level of education": "Education",
    "Working status": "Working status",
}

DEPRIVATION_ORDER = [
    "Most deprived decile",
    "Second most deprived decile",
    "Third more deprived decile",
    "Fourth more deprived decile",
    "Fifth more deprived decile",
    "Fifth less deprived decile",
    "Fourth less deprived decile",
    "Third less deprived decile",
    "Second least deprived decile",
    "Least deprived decile",
]

WHOLE_ADULT = {"19+ yrs", "18+ yrs", "16+ yrs"}


def load_raw():
    df = pd.read_csv(RAW, low_memory=False)
    df = df[df["Indicator ID"].isin(INDICATORS)].copy()
    df["indicator"] = df["Indicator ID"].map(INDICATORS)
    return df


def assign_dimension(df):
    df = df.copy()
    has_category = df["Category Type"].notna()
    whole_adult = df["Age"].isin(WHOLE_ADULT)
    both_sexes = df["Sex"] == "Persons"

    df["dimension"] = np.select(
        [
            has_category,
            ~has_category & whole_adult & ~both_sexes,
            ~has_category & ~whole_adult,
            ~has_category & whole_adult & both_sexes,
        ],
        ["_category", "Sex", "Age", "_overall"],
        default=None,
    )

    df.loc[df["dimension"] == "_category", "dimension"] = df.loc[
        df["dimension"] == "_category", "Category Type"
    ].map(DIMENSIONS)

    df["subgroup"] = np.select(
        [df["dimension"] == "Sex", df["dimension"] == "Age"],
        [df["Sex"], df["Age"]],
        default=df["Category"],
    )

    overall = df[df["dimension"] == "_overall"].copy()
    df = df[df["dimension"].notna() & (df["dimension"] != "_overall")]
    return df, overall


def reshape(df):
    wide = df.pivot_table(
        index=["Time period", "dimension", "subgroup"],
        columns="indicator",
        values="Value",
        aggfunc="first",
    ).reset_index()
    wide.columns.name = None
    return wide.rename(columns={"Time period": "year"})


def add_benchmark(wide, overall):
    bench = (
        overall[overall["Age"].isin(WHOLE_ADULT)]
        .pivot_table(index="Time period", columns="indicator",
                     values="Value", aggfunc="first")
        .reset_index()
        .rename(columns={"Time period": "year"})
    )
    bench.columns.name = None
    bench = bench.rename(
        columns={c: f"england_{c}" for c in bench.columns if c != "year"}
    )
    return wide.merge(bench, on="year", how="left")


def engineer(df):
    df = df.copy()
    df["above_national_obesity"] = (
        df["pct_overweight_obese"] > df["england_pct_overweight_obese"]
    ).astype(int)
    df["activity_gap"] = df["pct_active"] - df["england_pct_active"]
    df["obesity_gap"] = df["pct_overweight_obese"] - df["england_pct_overweight_obese"]
    df["diet_gap"] = df["pct_5aday"] - df["england_pct_5aday"]
    rank = {v: i + 1 for i, v in enumerate(DEPRIVATION_ORDER)}
    df["deprivation_rank"] = df["subgroup"].map(rank)
    df["year_numeric"] = df["year"].str[:4].astype(int)
    return df


def report(df):
    print(f"\nPrepared dataset: {len(df):,} rows, {df.shape[1]} columns")
    print(f"Years: {df['year'].min()} to {df['year'].max()} "
          f"({df['year'].nunique()} survey years)")
    print("\nRows per dimension:")
    for dim, n in df["dimension"].value_counts().items():
        subgroups = df[df["dimension"] == dim]["subgroup"].nunique()
        print(f"  {dim}: {n:,} rows across {subgroups} subgroups")
    complete = df.dropna(subset=["pct_active", "pct_overweight_obese"])
    print(f"\nRows usable for modelling: {len(complete):,}")
    print("\nTarget balance (above national obesity):")
    print(complete["above_national_obesity"].value_counts().to_string())


def main():
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    raw = load_raw()
    labelled, overall = assign_dimension(raw)
    wide = reshape(labelled)
    wide = add_benchmark(wide, overall)
    final = engineer(wide)
    final.to_csv(OUT, index=False)
    report(final)
    print(f"\nSaved to {OUT}")


if __name__ == "__main__":
    main()