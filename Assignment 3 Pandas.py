import pandas as pd
import os
import numpy as np

script_dir = os.path.dirname(__file__)
petal_path = os.path.join(script_dir, "Petal_Data.csv")
sepal_path = os.path.join(script_dir, "Sepal_Data.csv")

petal = pd.read_csv(petal_path)
sepal = pd.read_csv(sepal_path)

petal = petal.rename(columns={
    "sample_id": "sample_id",
    "species": "species",
    "petal_length": "petal_length",
    "petal_width": "petal_width"
})

sepal = sepal.rename(columns={
    "sample_id": "sample_id",
    "species": "species",
    "sepal_length": "sepal_length",
    "sepal_width": "sepal_width"
})

iris = pd.merge(
    petal[["sample_id", "species", "petal_length", "petal_width"]],
    sepal[["sample_id", "species", "sepal_length", "sepal_width"]],
    on=["sample_id", "species"],
    how="inner"
)

print("\nCombined DataFrame (first 5 rows):")
print(iris.head())

vars_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
corr_matrix = iris[vars_cols].corr()

pairs = (
     corr_matrix.where(~np.tril(np.ones(corr_matrix.shape)).astype(bool))
    .stack()
)

print("\nSix unique correlations:")
print(pairs)

means = iris[vars_cols].mean()
medians = iris[vars_cols].median()
stds = iris[vars_cols].std()

print("\nOverall means:")
print(means)

print("\nOverall medians:")
print(medians)

print("\nOverall standard deviations:")
print(stds)

output_dir = script_dir

summary_rows = []

for (v1, v2), val in pairs.items():
    summary_rows.append({"section": "correlation", "variable": f"{v1} vs {v2}", "value": val})

for v in vars_cols:
    summary_rows.append({"section": "mean", "variable": v, "value": means[v]})
    summary_rows.append({"section": "median", "variable": v, "value": medians[v]})
    summary_rows.append({"section": "std", "variable": v, "value": stds[v]})

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(os.path.join(output_dir, "iris_summary.csv"), index=False)

