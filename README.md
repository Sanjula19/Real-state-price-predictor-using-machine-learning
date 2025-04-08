<h1 align="center">
  🏠 Real Estate Price Predictor
</h1>

<h3 align="center">
  A Machine Learning Web App to Predict Real Estate Prices with Flask & Scikit-Learn
</h3>


## 🎥 Demo
![1](https://github.com/user-attachments/assets/80d4d34a-af0f-47d7-aca5-8be19950275d)

🚧 

---

## ✨ Features

- 🔍 Predicts property prices based on location, size, beds, and baths
- 📍 Dynamic dropdowns for District and Town
- 🧮 Handles multiple input features: land size, house size, beds, baths, etc.
- 🌐 Responsive UI built using HTML/CSS/JS
- 🔗 Flask backend with API integration
- 🧼 One-hot encoding and data preprocessing
- ❗ Error handling for invalid inputs

---

## ⚙️ Tech Stack

### 🖥 Frontend
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" width="40" height="40" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" width="40" height="40" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="40" height="40" />
</p>

### 🧠 Backend & ML
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="40" height="40" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="40" height="40" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="40" height="40" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="40" height="40" />
</p>

---

🧠 How it Works

📝 User enters property data (location, size, beds, etc.)

🚀 JavaScript sends the form data to the Flask /predict endpoint

⚙️ Backend performs preprocessing and encoding

🧠 Model predicts price using RandomForestRegressor

📊 Prediction is returned and displayed on the page


---

🧪 Model Training

python app.py

Make sure your dataset includes the following columns:

Beds,
Baths,
House_size,
Land_size,
District,
Town,
Price

The script will:

Preprocess the dataset ,
Encode categorical values ,
Train a RandomForestRegressor ,
Save the model as predictor_02.pickle

---





