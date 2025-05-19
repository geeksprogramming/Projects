# System Architecture – Cost of Living Predictor

This project combines visual and economic data to predict a country's cost of living.

---

## 1. Data Sources

- **Vision Dataset** (Kaggle Furniture Images)
  - Classes: `book`, `chair`, `laptop`
  - Represents low, mid, and high-tech lifestyle indicators
- **Economic Dataset** (CSV)
  - Fields: `income_index`, `cost_of_living_index`, `urbanization_score`, etc.

---

## 2. Workflow Overview

### Step 1: Image Classification
- CNN model classifies each image into one of three categories
- Output: `vision_category` (e.g., laptop)

### Step 2: Data Merge
- `simulate_merge()` combines vision predictions with DSP-style economic data
- Each image gets paired with an appropriate income-tier country

### Step 3: Feature Engineering
- Encodes `vision_category` and `urbanization_score`
- Adds:
  - `cost_to_income`
  - `income_rolling`
  - `cost_lag1`
  - `region_income_mean`

### Step 4: Model Training
- Regression models used:
  - `RandomForestRegressor` (final model)
  - XGBoost, Ridge (used for experimentation)
- Evaluation metrics:
  - R² Score
  - RMSE
  - Simulation with "laptop-only lifestyle" scenario

---

## 3. Deployment Paths

- `Streamlit` app: User interface for predictions via sliders/dropdowns
- (Optional) `FastAPI`: REST API backend with JSON input/output

---

## 4. Files and Modular Components

| File | Purpose |
|------|---------|
| `data_loader.py` | Load and clean DSP-style data |
| `feature_engineer.py` | Encode and compute new features |
| `model_train.py` | Train, evaluate, and save models |
| `app.py` | Streamlit UI |
| `model_config.yaml` | Central config for training & I/O |
| `README.md` | Project overview |
| `requirements.txt` | Dependency setup |
| `LICENSE` | Project license (MIT) |

---

## 5. Outputs

- Saved model: `best_rf_model.pkl`
- Encoders: `le_vision.pkl`, `le_region.pkl`
- Final merged dataset
- Charts (in `visualizations/`)

---