![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![IBM](https://img.shields.io/badge/IBM-052FAD?style=for-the-badge&logo=ibm&logoColor=white)

# 📊 Global Technology Trends & Developer Insights Analysis

**Data Analysis of Stack Overflow Developer Survey 2019 (88,883 Developers)**

---

## 🛠 Project Update

This repository previously contained only a README, a presentation PDF, and dashboard
screenshots — no dataset and no code. **This revision adds the actual notebook**
(`Tech_Trends_Analysis.ipynb`) that produces every chart and insight referenced below,
built directly from the public Stack Overflow Developer Survey 2019 data.

---

## 📌 Business Problem

Technology is evolving rapidly, making it difficult for organizations, developers, and
educators to identify which skills and tools will remain relevant in the future.

This project analyzes global developer survey data to identify **current technology
usage, emerging trends, and future skill demand**, enabling informed decision-making in
hiring, learning, and technology adoption.

---

## 🎯 Objectives

* Analyze current usage of programming languages and databases
* Identify emerging technologies gaining popularity
* Compare current usage vs future learning preferences
* Understand how developer demographics shape the survey sample
* Provide actionable insights for businesses and individuals

---

## 📂 Dataset

* **Source:** [Stack Overflow Developer Survey 2019](https://survey.stackoverflow.co/) (public release)
* **Size:** 88,883 developer responses, 85 columns (this analysis uses 9 of them)
* **Not included in this repo** due to file size (~190MB). Run `get_dataset.py` to
  rebuild it locally — see **Reproducing This Analysis** below.

### Key Features Used

* `LanguageWorkedWith` / `LanguageDesireNextYear` — current vs. desired programming languages
* `DatabaseWorkedWith` / `DatabaseDesireNextYear` — current vs. desired databases
* `Age`, `EdLevel`, `Country` — demographics

### Limitations

* Self-reported survey data — subject to reporting bias
* Multi-select fields show adoption *breadth*, not depth of use or proficiency
* Respondent base skews toward the US, India, Germany, and the UK

---

## 🛠 Tools & Technologies

* **Python:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook
* **Version Control:** Git & GitHub

---

## 🔍 Methodology

1. Reconstructed the full survey dataset from column-chunked source files (see `get_dataset.py`)
2. Selected the relevant columns and checked for missing values
3. Removed implausible Age outliers (self-reported noise, e.g. age 1 or 99) without
   imputing — invalid entries were dropped, not guessed at
4. Exploded semicolon-separated multi-select fields into per-technology counts
5. Compared current usage vs. future interest for languages and databases
6. Visualized demographic composition of the respondent base

---

## 📊 Key Insights

*(All figures below are computed directly in the notebook — see `Tech_Trends_Analysis.ipynb`)*

### 💻 Programming Language Trends

* JavaScript, HTML/CSS, and SQL are the most-used languages today, but their
  current-to-future growth is flat
* **Python jumps from the 4th most-used language to the 2nd most *desired*** — the
  clearest upward signal in the dataset
* TypeScript and Go show strong future-interest growth relative to current adoption

### 🗄 Database Trends

* MySQL leads current usage, but **PostgreSQL is the #1 *desired* database next year**
* Legacy enterprise databases (Oracle, Microsoft SQL Server) show comparatively low
  future interest relative to current usage

### 👨‍💻 Developer Demographics

* Median respondent age is ~29, with the middle 50% falling between 24 and 35
* Bachelor's and Master's degree holders make up the majority of respondents
* Respondents are concentrated in the United States, India, Germany, and the UK —
  a reason to describe these as *this sample's* trends, not universal global trends

---

## 📊 Dashboard

![Dashboard 1](images/dashboard_1_current_usage.png)
![Dashboard 2](images/dashboard_2_future_trends.png)
![Dashboard 3](images/dashboard_3_demographics.png)

---

## 💡 Business & Career Recommendations

* Organizations should prioritize Python and PostgreSQL in hiring/training pipelines,
  given their strong forward momentum
* Developers should treat JavaScript/HTML/CSS as baseline skills and differentiate with
  growth-trending tools
* Companies should sanity-check any "global" claim from this dataset against the
  country distribution — it's a Western/English-speaking-leaning sample

---

## 🔁 Reproducing This Analysis

```bash
pip install pandas numpy matplotlib seaborn
python get_dataset.py          # rebuilds dataset.csv (~190MB) from public source data
jupyter notebook Tech_Trends_Analysis.ipynb
```

---

## 🏁 Conclusion

This analysis demonstrates how survey data can be turned into concrete technology
investment signals — separating what's currently dominant from what's actually gaining
ground, which is the more useful question for hiring and training decisions.
