# Cost of Living Predictor – Vision + Economic AI System

This project combines lifestyle images and economic indicators to predict a country's cost of living using machine learning.

---

## Overview

We use a two-part pipeline:

1. **Vision Classification**: A CNN classifies lifestyle images (e.g., book, chair, laptop) into economic tiers.
2. **Economic Forecasting**: Country-level income, region, and vision category are used to predict the cost of living with a regression model.

The model is deployed using a user-friendly **Streamlit UI** for prediction.

---

## Folder Structure

```
cost-of-living-predictor/
│
├── app.py                            
├── requirements.txt                  
├── README.md                         
├── LICENSE                          
│
├── notebooks/
│   └── pixels_to_purchasing.ipynb    
│
├── scripts/                          
│   ├── data_loader.py                
│   ├── feature_engineer.py           
│   └── model_train.py                
│
├── data/
│   └── Cost_of_Living_and_Income.csv
│   └── Furniture and Essentials Image Dataset Link .txt
│
├── outputs/
│   ├── vision_predictions.csv        
│   ├── merged_vision_finance.csv     
│   ├── best_rf_model.pkl            
│   ├── le_vision.pkl                 
│   ├── le_region.pkl                        
│
├── visualizations/                   
│   ├── streamlit_ui_demo.png          
│   └── vision_category_distribution.png
│   └── correlation_matrix.png
│   └── cost_spread_by_vision.png
│   └── cv_r2_barplot.png
│   └── Income vs cost of living vs category.png
│   └── income_density_by_vision.png
│   └── laptop_lifestyle_shift.png  
│   └── income_vs_cost_by_vision.png       
│
├── config/
│   └── model_config.yaml             
│
└── docs/
    └── architecture.md               
```

---

## How to Use

### 1. Clone and install dependencies
```bash
git clone https://github.com/yourusername/cost-of-living-predictor.git
cd cost-of-living-predictor
pip install -r requirements.txt
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```

You can also run it in Google Colab using:
```python
!streamlit run app.py &
from pyngrok import ngrok
public_url = ngrok.connect(8501).public_url
print(public_url)
```

---

## Model Features

- `income_index`
- `vision_code` (encoded: book, chair, laptop)
- `urbanization_code` (region label)
- `cost_lag1` (last month’s cost)
- `income_rolling` (5-period moving average)

---

## Input Categories

| Vision Category | Implied Lifestyle Tier |
|------------------|------------------------|
| `book`           | Low income             |
| `chair`          | Middle income          |
| `laptop`         | High income            |

---

## Outputs

The model predicts:
```
Estimated Cost of Living: ₹xxxx.xx
```

---

## 📄 License

This project is licensed under the MIT License.

---

## Acknowledgments

- Kaggle Furniture Image Dataset
- Simulated DSP-style economic indicators
- Streamlit and FastAPI open-source tools

