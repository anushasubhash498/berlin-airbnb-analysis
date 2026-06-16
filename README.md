# Berlin Airbnb Market Analysis & Intelligence Dashboard

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-2.0+-navy.svg)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-red.svg)](https://www.tableau.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end data analytics and business intelligence project exploring the Airbnb market dynamics in Berlin. This repository features comprehensive Exploratory Data Analysis (EDA) in Python, statistical insights on pricing factors, and a premium interactive HTML/JS dashboard representing operational benchmarks.

---

## 🎯 Key Business Findings & Insights

- **Neighbourhood Premium**: **Mitte** and **Charlottenburg** command the highest listing premiums, averaging **€154.20** and **€140.50** respectively, driven by central proximity and cultural attractions.
- **Budget Corridors**: **Wedding** and **Lichtenberg** remain the most cost-effective alternatives, offering average listing rates below **€80.00**.
- **Room Preference**: **Entire home/apartments** represent **60.0%** of all available listings, reflecting a high customer preference for privacy and full unit utilization.
- **Superhost Price Advantage**: Superhosts command a **~26.3% price premium** (average €116.40 vs €92.10) and maintain higher overall rating scores (average 4.82/5.0 vs 4.45/5.0).
- **Availability Density**: Shared and hotel-style listings show significantly higher annual availability (280+ days), indicating lower overall occupancy compared to entire apartments/homes.

---

## 💻 Tech Stack

- **Data Wrangling & Processing**: `Python 3`, `pandas`, `numpy`
- **Visualization & Storytelling**: `matplotlib`, `seaborn`
- **Interactive UI**: `HTML5`, `CSS3 (Vanilla Glassmorphism)`, `JavaScript`, `Chart.js`
- **Database Concepts**: `PostgreSQL` structure representation

---

## 📂 Project Structure

```text
berlin-airbnb-analysis/
├── data/
│   ├── generate_data.py          # Script to generate representative listing dataset
│   └── berlin_listings.csv       # Dataset with 1000 listings
├── notebooks/
│   └── berlin_airbnb_analysis.py # Python script for EDA & image generation
├── outputs/
│   ├── price_by_neighbourhood.png
│   ├── room_type_distribution.png
│   ├── superhost_comparison.png
│   ├── price_vs_rating.png
│   └── availability_heatmap.png
├── dashboard/
│   └── index.html                # Interactive glassmorphism dashboard
├── requirements.txt              # Project library dependencies
└── README.md                     # Project summary and documentation
```

---

## ⚙️ How to Run Locally

### 1. Set Up Environment
```bash
# Clone the repository
git clone https://github.com/anushasubhash498/berlin-airbnb-analysis.git
cd berlin-airbnb-analysis

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate Dataset & Run Analysis
```bash
# Run data generator
python data/generate_data.py

# Run analysis and output plots
python notebooks/berlin_airbnb_analysis.py
```

### 3. Open Interactive Dashboard
Open `dashboard/index.html` in any web browser to view the interactive dashboard with filters and responsive Chart.js visual graphs.

---

## 👤 About the Author
**Anusha Subhash**  
Candidate for **Data Analyst** and **Business Analyst** positions in Berlin.  
BSc in Computer Science & Digitisation.  
Experienced with SQL database management, Tableau visualization, and statistical programming in Python.
