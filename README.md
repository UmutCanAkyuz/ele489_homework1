# ELE489 HW1 – KNN on the Wine Dataset

**Author:** Umut Can Akyüz

**Course:** ELE489 – Fundamentals of Machine Learning  
**Institution:** Hacettepe University

---

## Overview

This repository contains the code and analysis for Homework 1 of the ELE489 course, where the K-Nearest Neighbors (KNN) algorithm is studied and implemented. The objective is twofold:
1. Build a custom KNN classifier (supporting Euclidean and Manhattan distances).
2. Compare it against the KNN classifier available in Scikit-learn.

The dataset chosen is the well-known **Wine Dataset** from the UCI Machine Learning Repository.

---

## Repository Contents

- **knn.py**  
  Houses the custom KNN classifier implementation. It supports both Euclidean and Manhattan metrics.
- **analysis.ipynb**  
  A Jupyter Notebook providing:
  - Data loading and exploratory analysis
  - Visualizations (pair plots, KDE plots, etc.)
  - Data preprocessing steps (e.g., normalization)
  - KNN experiments across various values of \(k\)
  - Comparative results between custom KNN and Scikit-learn’s built-in implementation
- **wine.data**  
  The Wine dataset (13 numeric features, 3 classes, 178 samples) must be in the same directory for the code to function properly.
- **README.md**  
  This file, providing a summary of the project structure, dataset, and instructions.

---

## Dataset Details

- **Name**: UCI Wine Dataset  
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/109/wine)  
- **Samples**: 178  
- **Features**: 13 numeric attributes  
- **Target Classes**: 3 distinct wine cultivars, labeled as 1, 2, and 3  

---

## Implemented Features

1. **Data Loading & EDA**  
   - Imports the dataset, checks for missing values, and visualizes the data distribution.
2. **Visualization**  
   - Uses Seaborn and Matplotlib for KDE plots, boxplots, and pairplots.
3. **Data Preprocessing**  
   - Applies **StandardScaler** for normalization.
   - Splits data into 80% training and 20% testing sets.
4. **Custom KNN Classifier**  
   - Supports **Euclidean** and **Manhattan** distance metrics.
   - Evaluates accuracy across a range of \(k\) values (1 through 30).
5. **Performance Evaluation**  
   - Generates confusion matrices and classification reports.
   - Compares the custom KNN approach with Scikit-learn’s `KNeighborsClassifier`.
   - Analyzes the match rate of predictions between both implementations.

---

**Outputs:**  
- Accuracy plots for each \(k\), comparing distance metrics.  
- Confusion matrices and classification reports for selected \(k\) values.  
- Analysis of how closely the custom classifier matches the built-in `KNeighborsClassifier`.

---

## Instructor & Course

- **Course**: ELE489 – Fundamentals of Machine Learning  
- **Instructor**: Prof. Seniha Esen Yüksel  
- **Department**: Electrical and Electronics Engineering, Hacettepe University

---

## References

- **UCI Wine Dataset**: [UCI Repository](https://archive.ics.uci.edu/dataset/109/wine)  
- **Scikit-learn**: [Documentation](https://scikit-learn.org/stable/)  
- **KNN Tutorial**: [Kaggle Example](https://www.kaggle.com/code/prashant111/knn-classifier-tutorial)  
- **Confusion Matrix**: [W3Schools Explanation](https://www.w3schools.com/python/python_ml_confusion_matrix.asp)

---
