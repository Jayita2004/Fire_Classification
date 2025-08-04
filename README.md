# 🔥 Fire Type Classification in India (2021–2023) using MODIS Data

This project leverages MODIS satellite data from NASA's Terra and Aqua satellites to classify different types of fire events across India from 2021 to 2023.

---

## Overview

- **Data Source:** MODIS (via NASA FIRMS)  
- **Time Period:** 2021 to 2023  
- **Region:** India  
- **Objective:** Automatically classify fire types (e.g., vegetation, agriculture, volcanic, etc.)  
- **Tools & Libraries:** Python, Pandas, Seaborn, Scikit-learn, XGBoost, Folium
- **Deployment(Locally):** Streamlit 

---

## Contents

- `Fire_Classification.ipynb` — Complete code and analysis notebook  
  Includes data preprocessing, visualization, model training, and mapping of fire incidents
- `modis_2021_India.csv`, `modis_2022_India.csv`, `modis_2023_India.csv` — Year-wise fire datasets
- `app.py` — Example script for loading trained model and running predictions
- `.gitignore` — Prevents accidental commits of large files and virtual environments

---

## Project Completion Summary

This project has successfully:

- Loaded and merged multi-year MODIS fire data
- Performed extensive EDA and visualization
- Encoded and cleaned categorical variables
- Applied feature selection (`SelectKBest`, `mutual_info_classif`)
- Built and evaluated multiple classification models:
  - Logistic Regression
  - Random Forest
  - XGBoost
- Visualized fire incidents across India using **folium**
- Achieved satisfactory model performance metrics (accuracy, confusion matrix, classification report)

---

## Why Model Files Are Not in This Repository

The trained model files (`.pkl`) exceed GitHub’s 100MB file size limit.  
To avoid repository bloat and comply with GitHub storage policies, they are hosted externally.  
This ensures that the repository remains clean and easy to clone.

## Download Pre-trained Models

You can download the trained models here:

🔗 **[Download Best_fire_detection_model.pkl](https://drive.google.com/file/d/1gbOTbF169Hi37KLYfZjNykaOrkvv1Av_/view?usp=sharing)**

🔗 **[Download scaler.pkl](https://drive.google.com/file/d/1ghIQx3yQkdZnOAPtnp0mp_jpmrH5NMUu/view?usp=sharing)**

After downloading, place them in the project root folder to use for inference.

---

## Getting Started

To run this project:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jayita2004/Fire_Classification.git

2. **Run command** 
     cd Fire_Classification
