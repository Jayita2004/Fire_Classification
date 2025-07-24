# 🔥 Fire Type Classification in India (2021–2023) using MODIS Data

This project leverages MODIS satellite data from NASA's Terra and Aqua satellites to classify different types of fire events across India from 2021 to 2023.
---
## Overview

- **Data Source:** MODIS (via NASA FIRMS)  
- **Time Period:** 2021 to 2023  
- **Region:** India  
- **Objective:** Classify fire types (e.g., vegetation, agriculture, volcanic, etc.)  
- **Tools:** Python, Pandas, Seaborn, Scikit-learn
---
## Contents
- `Fire_Classification.ipynb`: Google Colab notebook containing complete code and analysis  
   Includes data preprocessing, visualization, and ML model development  
   Now includes folium map rendering fire points on India’s map
- `modis_2021_India.csv`, `modis_2022_India.csv`, `modis_2023_India.csv`: Year-wise fire data files
---
## Progress So Far

### Week 1:
- Imported necessary libraries and loaded the MODIS fire dataset
- Performed basic data checks (`info()`, `isnull()`, `duplicated()`)
- Explored categorical columns and fire type distributions
- Plotted a bar chart of fire types using `countplot`
- Visualized the distribution of confidence scores using a histogram with KDE

### Week 2 (NEW):
- Cleaned and encoded categorical data
- Merged all year-wise datasets into a single DataFrame
- Applied feature selection using `SelectKBest` and `mutual_info_classif`
- Built classification models: Logistic Regression, Random Forest, XGBoost
- Visualized fire incidents using **folium** (map of fire locations across India)
- Evaluated models with accuracy, confusion matrix, and classification report
---
## Getting Started
To run this notebook:

1. Clone the repository  
2. Open `Fire_Classification.ipynb` in **Google Colab** or Jupyter Notebook  
3. Install required libraries:  
   `pandas`, `seaborn`, `scikit-learn`, `folium`, `xgboost`
---
## Open in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jayita2004/Fire_Classification/blob/main/Fire_Classification.ipynb)

---

