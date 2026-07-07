# 🏦 Loan Approval Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a loan application will be **Approved** or **Rejected** using Machine Learning algorithms. The complete pipeline includes data preprocessing, feature selection, model training, hyperparameter tuning, and deployment using Streamlit.

---

## 🚀 Live Demo

🔗 Streamlit App:(https://loanpredictioner.streamlit.app/)

---

## 📊 Dataset Information

- Records: 4,269
- Features: 13
- Target Variable:
  - Approved
  - Rejected

### Features

- Number of Dependents
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Asset Value
- Education
- Self Employed

---

# 🔍 Data Preprocessing

✔ Checked Missing Values

✔ Checked Duplicate Records

✔ Checked Data Types

✔ Checked Outliers

✔ Handled Negative Asset Values

✔ One-Hot Encoding

✔ StandardScaler

---

# 📈 Exploratory Data Analysis

Performed EDA using

- Distribution Plots
- Count Plots
- Box Plots
- Correlation Analysis

---

# 📌 Feature Selection

### Pearson Correlation

Used Pearson Correlation to analyze numerical features.

### Chi-Square Test

Used Chi-Square Test for categorical features.

Dropped Features

- education
- self_employed

because they had very high p-values and contributed very little to prediction performance.

---

# 🤖 Machine Learning Models

- Logistic Regression
- K-Nearest Neighbors
- Naive Bayes
- Decision Tree
- Support Vector Machine
- Random Forest
- XGBoost

---

# ⚙ Hyperparameter Tuning

Used

- GridSearchCV
- RandomizedSearchCV

Best Parameters

```
max_depth = None

min_samples_split = 2

n_estimators = 100
```

---

# 🏆 Final Model

Random Forest Classifier

### Performance

Accuracy : **98.01%**

F1 Score : **97.31%**

---

# 🌐 Deployment

The project has been deployed using **Streamlit Community Cloud**.

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

# 📁 Project Structure

```
Loan-Approval-Prediction
│
├── app.py
├── loan_project.ipynb
├── loan_model.pkl
├── scaler1.pkl
├── feature_names.pkl
├── requirements.txt
└── README.md
```

---

# 📷 Screenshots

(Add screenshots here)

- Home Page
- Prediction Result
- Confusion Matrix
- Feature Importance

---

# ⭐ Future Improvements

- Deploy using Docker
- Build REST API using FastAPI
- Add Explainable AI (SHAP)
- Improve UI/UX
- Add Authentication

---

# 👨‍💻 Author

**Raghav Pratap**

B.Tech Computer Science Engineering

Gautam Buddha University

GitHub: https://github.com/meraghav18
