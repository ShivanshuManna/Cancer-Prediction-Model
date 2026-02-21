🧬 Cancer Risk Assessment Web Application

A Machine Learning based web application built using Flask that predicts cancer stage based on selected health and lifestyle factors.

🚀 Overview

This project uses a trained machine learning model to analyze user inputs and predict the cancer stage.

The application provides a clean medical-style interface and displays results in a professional popup dialog.

📊 Input Parameters

The model takes the following inputs:

Genetic Risk (0 – 10)

Air Pollution Level (0 – 10)

Alcohol Use (0 – 10)

Smoking Level (0 – 10)

Obesity Level (0 – 10)

The model predicts:

Stage 0

Stage 1

Stage 2

Stage 3

🛠️ Technologies Used

Python

Flask

NumPy

Scikit-learn

HTML5

CSS3

Pickle

📂 Project Structure
│── app.py
│── model.pkl
│── train_model.py
│── templates/
│     └── cancer.html
│── README.md
⚙️ How It Works

User enters health-related values.

Data is sent to the Flask backend.

The trained model predicts a numeric stage.

A mapping function converts numeric output into:

Stage 0

Stage 1

Stage 2

Stage 3

The result is displayed in a modal popup.

▶️ How To Run The Project
1. Clone the repository
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Install dependencies
pip install flask numpy scikit-learn
3. Run the application
python app.py
4. Open in browser
http://127.0.0.1:5000
🎯 Features

✔ Medical-themed professional UI
✔ Decimal input handling
✔ Input validation
✔ Stage mapping for user-friendly output
✔ Flask deployment ready

⚠ Disclaimer

This tool provides predictive analysis based on model training data.
It is not a medical diagnosis and should not replace professional medical advice.

👨‍💻 Author

Shivanshu Manna
