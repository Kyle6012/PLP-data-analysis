# Assignment: Data Analysis and Visualization with Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


# Task 1: Load and Explore Dataset

try:
    # load iris dataset
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame

    print("Dataset loaded successfully\n")
except Exception as e:
    print("Error loading dataset:", e)

# show first few rows
print("First five rows of dataset:")
print(df.head())

# check data types and missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# clean dataset 
df = df.fillna(df.mean(numeric_only=True))

# Task 2: Basic Data Analysis

# basic statistics
print("\nStatistical summary:")
print(df.describe())

# group by target (species)
print("\nAverage measurements by species:")
grouped = df.groupby("target").mean()
print(grouped)

# finding: Iris species have different mean petal/sepal sizes
# could suggest clear separability

# Task 3: Data Visualization


plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart of Sepal and Petal Lengths")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# bar chart: average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x="target", y="petal length (cm)", data=df, ci=None, palette="Set2")
plt.title("Average Petal Length by Species")
plt.xlabel("Species (0=setosa,1=versicolor,2=virginica)")
plt.ylabel("Petal Length (cm)")
plt.show()

# histogram of sepal width
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# scatter plot: sepal length vs petal length
plt.figure(figsize=(6,5))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

print("\nObservations:")
print("- Different iris species show distinct mean petal and sepal lengths.")
print("- Histogram shows sepal width is roughly normally distributed.")
print("- Scatter plot reveals clusters by species, suggesting separability.")
