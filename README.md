# SMS Spam Detector 📩

A machine learning-based web application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP).

## 📌 Project Overview

SMS Spam Detector analyses text messages using a trained machine learning model and identifies messages that may be spam. It also performs simple rule-based checks to highlight potential warning signs, such as suspicious links, urgent language, and requests for sensitive information.

The application provides an interactive interface built using Streamlit.

## ✨ Features

- **SMS Classification:** Predicts whether a message is spam or ham.
- **Text Processing:** Uses TF-IDF to convert text into numerical features.
- **Machine Learning:** Uses a trained Logistic Regression classifier.
- **Security Warning Indicators:** Highlights selected patterns that may indicate suspicious messages.
- **Interactive UI:** Allows users to enter and analyse messages through a Streamlit web application.

## 🛠️ Technologies Used

- Python
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Joblib
- Regular Expressions (Regex)

## 📂 Project Structure

```text
SMS-Spam-Detector/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── sms_cyber_threat_model.pkl
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/Hasi0402/SMS-Spam-Detector.git
cd SMS-Spam-Detector
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📊 Dataset

The model was trained using the **UCI SMS Spam Collection** dataset, which contains SMS messages labelled as spam or ham.

## ⚙️ How It Works

1. The user enters an SMS message in the Streamlit interface.
2. The trained TF-IDF and Logistic Regression pipeline processes the message.
3. The model predicts whether the message is spam or ham.
4. Additional rule-based checks identify selected warning indicators.
5. The application displays the prediction and any detected warnings.

## ⚠️ Limitations

- The model may misclassify messages.
- Security warning indicators are simple rule-based checks, not a separate machine learning-based cyber threat detector.
- The application does not verify URLs against live threat databases.
- A message classified as ham is not guaranteed to be safe.

This project is intended for educational and demonstration purposes.

## 👩‍💻 Author

**Hasiba Aisha I.**

GitHub: [@Hasi0402](https://github.com/Hasi0402)
