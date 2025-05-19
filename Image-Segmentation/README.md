# Semantic Segmentation with U-Net (Furniture & Essentials Dataset)

This repository provides a complete solution for semantic segmentation using a U-Net architecture trained on a subset of the **Lyft Udacity Self-Driving Car Dataset** (adapted as a proxy for furniture and essentials).

---

## Project Directory Structure

```

ml_project/
├── data/                             
│   └── dataset link.txt
├── docs/                             
│   └── architecture.txt
│   └── approach.md
├── problem_statement/
│ └── problem.md
├── solution/ 
│ └── Solution.ipynb
├── src/
│  ├── data_loader.py           
│  ├── model_unet.py             
│  ├── train_unet.py             
│  └── evaluate_unet.py          
├── tests/
│   └── test_unet.py  
├── visualisation/
│   └── visualisation.png
│   └── visualisation.png
│   └── visualisation.png 
│   └── visualisation.png
├── requirements.txt                  
└── LICENSE                           
```

---

## Setup Instructions

To configure your local environment, follow these clear steps:

1. **Set up a Python virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Use venv\Scripts\activate for Windows
   ```

2. **Install project dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Model Training

Initiate training with the following command:

```bash
python src/train_unet.py
```

Ensure your dataset directories:

* RGB Images: `./data/carla/CameraRGB/`
* Segmentation Masks: `./data/carla/CameraSeg/`

---

## Model Evaluation

Evaluate your trained model by importing the evaluation script:

```python
from src.segmentation.evaluate_unet import evaluate_model

# Example usage (customize as needed)
evaluate_model(model_path='path/to/saved/model')
```

## Project Dependencies

All libraries and dependencies required by this project are neatly organized in the `requirements.txt` file.

---

## Licensing

This project uses the **MIT License**, which allows you to:

* Freely use and modify the software commercially or non-commercially.
* Distribute copies, including modified versions.
* Integrate this software into proprietary products.

You must include the original copyright notice and a copy of the license text in any redistribution. See the LICENSE file for details.