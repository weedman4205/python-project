# Exploratory Data Analysis on Air Pollution Dataset

This project presents an in-depth **Exploratory Data Analysis (EDA)** on an air pollution dataset from various Indian cities. It focuses on identifying pollution patterns, visualizing pollutant concentrations, and applying a regression model to derive actionable insights.

## 📌 Project Overview

- **Course:** DATA SCIENCE TOOLBOX: PYTHON PROGRAMMING (INT375)
- **Author:** Shikhar Agrawal
- **Institution:** Lovely Professional University
- **Semester:** January - April 2025
- **Supervisor:** Ms. Maneet Kaur

## 🧠 Objectives

- Understand trends and hotspots in air pollution data.
- Visualize pollutant types, city-wise and state-wise distributions.
- Examine the relationship between pollutant values using correlation and regression.
- Identify outliers and clusters in pollution levels.
- Explore geographical patterns using latitude and longitude.

## 🗃️ Dataset

- Source: Provided by the university.
- Format: CSV
- Fields include: `state`, `city`, `latitude`, `longitude`, `pollutant_id`, `pollutant_min`, `pollutant_max`, `pollutant_avg`, `last_update`, and more.

## 🛠️ Technologies Used

- **Python**
- **Libraries:**
  - `pandas`, `numpy` for data handling
  - `matplotlib`, `seaborn` for visualizations
  - `scikit-learn` for modeling

## 📊 Key Analysis & Visualizations

### 1. Pollutant Type Frequency
- Sorted bar chart showing count of each pollutant type.

### 2. Top 10 Polluted Cities
- Horizontal bar chart of cities with highest average pollution.

### 3. State-wise Pollution Levels
- Box plots showing pollutant distribution across states.

### 4. Correlation Analysis
- Heatmap showing correlations between `pollutant_min`, `pollutant_max`, and `pollutant_avg`.

### 5. Outlier Detection
- Box plots by pollutant type.

### 6. Geographic Visualization
- Scatter plots mapping pollution levels using `latitude` and `longitude`.

### 7. Grouped Bar Charts
- Comparing pollution levels across top cities for different pollutants.

### 8. Distribution Plot
- Histogram + KDE for `pollutant_avg`.

### 9. Scatter Plot Matrix
- Pair plots with pollution categories (`Low`, `Medium`, `High`).

### 10. Linear Regression Modeling
- Predicting `pollutant_avg` using `pollutant_max` with:
  - **R² Score ~ 0.9**
  - **MSE** for error evaluation

## 🤖 Code Structure

- **Data Cleaning:** Missing value imputation, duplicates removal, date conversion, categorical noise reduction.
- **EDA:** Visualizations for trends and patterns.
- **Modeling:** Linear regression with evaluation metrics.

