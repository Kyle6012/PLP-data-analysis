# Data Analysis Assignment

## Overview

For this assignment, I worked with the **Iris dataset**. The goal was to practice loading data, cleaning it, analyzing it with **pandas**, and then making visualizations with **matplotlib** and **seaborn**. I wrote everything inside `main.py` and set up a `pyenv` environment called **analysis** so it’s easy to reproduce.

---

## Dataset Used

I chose the **Iris dataset** because it is simple but also useful for analysis. It has 150 samples of iris flowers from three species (*setosa*, *versicolor*, and *virginica*). Each sample has:

* Sepal length (cm)
* Sepal width (cm)
* Petal length (cm)
* Petal width (cm)
* Target (species label: 0 = setosa, 1 = versicolor, 2 = virginica)

The dataset is available directly in scikit-learn, so no extra CSV file is needed.

---

## Requirements

* Python 
* Libraries:

  * pandas
  * matplotlib
  * seaborn
  * scikit-learn

---

## How to Run

1. Create and Activate the environment:

   ```bash
   pyenv virtualenv 3.12.5 analysis
   pyenv activate analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python main.py
   ```

---

## What the Program Does

* Loads the Iris dataset from scikit-learn
* Prints out the first rows, info, and missing values
* Cleans missing values (fills numeric columns)
* Shows a statistical summary
* Groups the data by species and calculates averages
* Creates four visualizations:

  1. Line chart of sepal vs petal length
  2. Bar chart of average petal length by species
  3. Histogram of sepal width
  4. Scatter plot of sepal length vs petal length with species coloring

## Assignment Mapping

* **Task 1: Load + Explore** → top of script (loading Iris, head, info, missing values)
* **Task 2: Analysis** → statistical summary and groupby by species
* **Task 3: Visualization** → the four seaborn/matplotlib plots with labels and titles
