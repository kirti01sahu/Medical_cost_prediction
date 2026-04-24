Medical Insurance Cost Prediction
This project uses Machine Learning to predict the medical insurance costs (charges) of individuals based on their personal attributes like age, BMI, and smoking habits.

Project Overview
The goal of this project is to analyze a dataset of medical insurance records and build a regression model that can accurately estimate insurance premiums. This can help insurance companies or individuals understand which factors contribute most to their medical expenses.

Dataset Features
The model uses the following information:

Age: Age of the primary beneficiary.

Sex: Gender (Male/Female).

BMI: Body Mass Index.

Children: Number of children/dependents.

Smoker: Whether the person smokes or not.

Region: Residential area.

Charges: Individual medical costs (The Target variable).

How it Works
Exploratory Data Analysis (EDA): I used histograms and heatmaps to visualize how factors like age and BMI affect insurance costs.

Data Preprocessing: Categorical data was converted into numbers using One-Hot Encoding so the model could understand it.

Model Building: I used a Linear Regression model to train on the data.

Evaluation: The model's performance was checked by comparing the "Actual" costs against the "Predicted" costs.

Tech Stack
Language: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn

How to Run
Download the medical_insurance.csv dataset.

Open the Medical_cost_prediction.ipynb file in Google Colab or Jupyter Notebook.

Run all cells to see the analysis and model results.
