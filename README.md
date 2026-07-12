# DeepShield 🛡️

DeepShield is a deep learning-based system that detects whether an image is **real** or **AI-generated/fake** (deepfake detection), built using OpenCV and a trained image classification model.

## 📌 Project Overview
This project was built as a major project to explore how deep learning models can be used to distinguish real photographs from AI-generated or manipulated images.

## 🗂️ Project Structure
```
DeepShield/
├── data/
│   ├── train/
│   │   ├── fake/
│   │   └── real/
│   ├── val/
│   │   ├── fake/
│   │   └── real/
│   └── test/
│       ├── fake/
│       └── real/
├── models2/
├── notebooks/
│   └── image_basics.ipynb
├── train.py
├── predict.py
├── sample.jpg
└── README.md
```

## ⚙️ Tech Stack
- Python
- OpenCV
- [add your ML framework here, e.g. TensorFlow / PyTorch / scikit-learn]
- Jupyter Notebook

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Sh-git07/DeepShield.git
cd DeepShield
```

### 2. Set up a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add the dataset
Download the dataset and place it inside a `data/` folder using the structure shown above.

### 5. Train the model
```bash
python train.py
```

### 6. Run predictions
```bash
python predict.py --image sample.jpg
```

## 📊 Results
[Add your model accuracy, confusion matrix, or sample output screenshots here]

## 📖 What Each File Does
- **train.py** — Loads the dataset, builds and trains the classification model, saves it to `models2/`
- **predict.py** — Loads a trained model and predicts whether a given image is real or fake
- **notebooks/image_basics.ipynb** — Notebook used to explore image preprocessing with OpenCV before building the full pipeline
- **data/** — Contains training, validation, and test images split into `real` and `fake` folders

## 🙋 Author
Made by Shikha Agnihotri 
