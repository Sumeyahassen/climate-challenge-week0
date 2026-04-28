````markdown
# 10 Academy: African Climate Trend Analysis (Week 0)

## 📋 Project Overview

This project is part of the **10 Academy Artificial Intelligence Mastery Program**.  
As a **Junior Data Analyst at EthioClimate Analytics**, I conducted an **Exploratory Data Analysis (EDA)** of historical climate data (**2015–2026**) for five African nations:

- Ethiopia
- Kenya
- Sudan
- Tanzania
- Nigeria

The objective is to provide **evidence-backed climate insights** to support **Ethiopia’s position as the host for COP32 in 2027**.

---

## 🚀 Features

###  Data Cleaning
- Processed NASA POWER climate datasets
- Removed metadata noise
- Replaced `-999` sentinel values with `NaN`

### 📈 Time-Series Analysis
- Monthly resampling of temperature and precipitation data
- Seasonal trend identification
- Climate variability exploration

### ⚙️ CI/CD Pipeline
- Implemented GitHub Actions workflow
- Automated dependency installation
- Continuous environment testing

### 🌍 Negotiation-Grade Insights
- Annotated visualizations for:
  - Peak heat events
  - Rainfall anomalies
  - Cross-country climate comparisons

---

## 📂 Folder Structure
```plaintext
├── app/                    # Dashboard Application
│   ├── main.py             # Streamlit entry point
│   └── utils.py            # Data processing & plotting logic
├── data/                   # Cleaned CSV files (Git ignored)
├── notebooks/              # Jupyter Notebooks (Task 1 & 2)
├── scripts/                # Python scripts for data fetching
├── .github/workflows/      # CI/CD (GitHub Actions)
├── requirements.txt        # Project dependencies
└── README.md

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sumeyahassen/climate-challenge-week0.git
cd climate-challenge-week0
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Key Insights

### 🌡️ Temperature Trends

* Upward trend in average temperatures across East Africa
* Significant heat anomalies detected in **2022**

### 🌧️ Precipitation Trends

* Identified peak rainy seasons
* High rainfall variability in:

  * Ethiopia
  * Sudan
  * Kenya
  * Tanzania
  * Nigeria

---

## 🤖 CI/CD Integration

This repository uses **GitHub Actions** for reproducibility.

On every push to the `main` branch, the workflow:

* Installs required packages
* Verifies Python environment
* Ensures project consistency

---

## 🧪 Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* GitHub Actions

---

## 🎯 Project Goal

Use historical climate evidence to strengthen **Ethiopia’s diplomatic case for hosting COP32 (2027)**.


---

## ✍️ Author

**Sumeya**
Software Developer |10 Academy Student

---

```
```
