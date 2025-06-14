# 🔥 Forest Fire Detection from Satellite Images

![Streamlit App Banner](https://img.shields.io/badge/Built%20with-Streamlit-red?style=for-the-badge&logo=streamlit)
![Model](https://img.shields.io/badge/Model-Keras%20CNN-blue?style=for-the-badge&logo=keras)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🌍 About the Project

**Forest Fire Detection** is a deep learning-based web application that analyzes satellite images to determine the presence of forest fires. It leverages a Convolutional Neural Network (CNN) model trained on fire and non-fire imagery to offer fast, reliable predictions through an interactive Streamlit interface.

🔗 [**Live App**](https://forestfire-nmvybtnnxnvcwbe6sregvg.streamlit.app/)

---

## 🚀 Features

- 📷 Upload satellite images directly
- 🧠 Predicts "Fire 🔥" or "No Fire"
- 📊 Displays confidence levels
- ⚡ Fast and lightweight interface
- ✅ Easy to deploy and use

---

## 🖼️ App Preview

| Upload Image | Prediction Result |
|--------------|-------------------|
| ![upload](https://github.com/devansh7444/Forest_Fire/blob/c58b2550df9338a9b0d16ed3b9329b95db179c0d/image.png) | ![result](https://via.placeholder.com/300x150.png?text=Prediction:+Fire+🔥) |

---

## 🧠 Model Details

- Framework: **TensorFlow/Keras**
- Architecture: **CNN**
- Input Shape: **64x64x3 RGB Images**
- Classes: `["No Fire", "Fire 🔥"]`
- Output: Softmax layer with confidence

---

## 📦 Installation & Usage

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fire-detection-app.git
   cd fire-detection-app
