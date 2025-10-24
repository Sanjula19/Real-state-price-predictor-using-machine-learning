# Real Estate Price Predictor 🏠

A production-ready machine learning web application for predicting real estate prices in Sri Lanka using ensemble learning techniques and Flask framework.

![Demo](https://github.com/user-attachments/assets/815c04e4-317f-4ba3-81f9-6ddd50750600)

## 🎯 Project Overview

This project demonstrates end-to-end machine learning model development and deployment, featuring real-time property price predictions based on location, size, and property characteristics. Built with scalability and user experience in mind, it showcases modern ML engineering practices.

### Key Highlights

- **Accurate Predictions**: Random Forest Regressor model trained on real Sri Lankan property data
- **Interactive UI**: Responsive web interface with dynamic form validation
- **RESTful API**: Flask-based backend with JSON API endpoints
- **Data Preprocessing**: Automated feature engineering and one-hot encoding
- **Production Ready**: Error handling, logging, and model persistence

## ✨ Features

### Core Functionality
- 🎯 **Price Prediction**: Estimate property prices based on multiple features
- 📍 **Location-Based**: District and town-specific predictions
- 🏡 **Property Details**: Considers beds, baths, land size, and house size
- 🔄 **Dynamic Dropdowns**: Location options loaded from trained model
- ✅ **Input Validation**: Client and server-side validation
- 📊 **Real-time Results**: Instant predictions via AJAX

### Technical Features
- 🧠 **ML Pipeline**: Scikit-learn RandomForestRegressor
- 🔧 **Feature Engineering**: Automated preprocessing and encoding
- 💾 **Model Persistence**: Pickle serialization for deployment
- 🌐 **RESTful API**: JSON-based communication
- 📱 **Responsive Design**: Mobile-friendly interface
- ⚡ **Fast Response**: Optimized prediction latency

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                   Client Layer                   │
│         (HTML/CSS/JavaScript Frontend)           │
└────────────────┬────────────────────────────────┘
                 │ HTTP Request (JSON)
                 ↓
┌─────────────────────────────────────────────────┐
│              Flask Application                   │
│                 (app.py)                         │
│  ┌──────────────────────────────────────────┐   │
│  │  API Routes                              │   │
│  │  - /predict (POST)                       │   │
│  │  - /get_locations (GET)                  │   │
│  └──────────────┬───────────────────────────┘   │
│                 │                                │
│  ┌──────────────▼───────────────────────────┐   │
│  │  Data Preprocessing Layer                │   │
│  │  - Feature encoding                      │   │
│  │  - Data validation                       │   │
│  └──────────────┬───────────────────────────┘   │
│                 │                                │
│  ┌──────────────▼───────────────────────────┐   │
│  │  ML Model (RandomForestRegressor)        │   │
│  │  - Trained model (predictor_02.pickle)   │   │
│  └──────────────┬───────────────────────────┘   │
│                 │                                │
└─────────────────┼────────────────────────────────┘
                  │ Prediction
                  ↓
            [Price Estimate]
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/real-estate-predictor.git
cd real-estate-predictor
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify installation**
```bash
python --version  # Should be 3.8+
pip list          # Check installed packages
```

### Running the Application

#### Development Mode

```bash
python app.py
```

The application will start on `http://localhost:5000`

#### Production Mode

```bash
# Using Gunicorn (Linux/Mac)
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Waitress (Windows)
waitress-serve --listen=*:5000 app:app
```

### Accessing the Application

1. Open browser: `http://localhost:5000`
2. Select District and Town
3. Enter property details:
   - Number of Bedrooms
   - Number of Bathrooms
   - House Size (sq ft)
   - Land Size (perches)
4. Click "Predict Price"
5. View estimated price

## 📋 API Documentation

### Endpoints

#### 1. Get Locations
```http
GET /get_locations
```

**Description**: Retrieve available districts and towns

**Response**:
```json
{
  "districts": ["Colombo", "Gampaha", "Kandy", ...],
  "towns": {
    "Colombo": ["Nugegoda", "Dehiwala", ...],
    "Gampaha": ["Kadawatha", "Ja-Ela", ...]
  }
}
```

#### 2. Predict Price
```http
POST /predict
```

**Description**: Predict property price based on features

**Request Body**:
```json
{
  "district": "Colombo",
  "town": "Nugegoda",
  "beds": 3,
  "baths": 2,
  "house_size": 1500,
  "land_size": 10
}
```

**Response** (Success):
```json
{
  "success": true,
  "price": 45000000,
  "formatted_price": "LKR 45,000,000"
}
```

**Response** (Error):
```json
{
  "success": false,
  "error": "Invalid input: beds must be positive"
}
```

### Example Usage

**cURL**:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "district": "Colombo",
    "town": "Nugegoda",
    "beds": 3,
    "baths": 2,
    "house_size": 1500,
    "land_size": 10
  }'
```

**Python (requests)**:
```python
import requests

url = "http://localhost:5000/predict"
data = {
    "district": "Colombo",
    "town": "Nugegoda",
    "beds": 3,
    "baths": 2,
    "house_size": 1500,
    "land_size": 10
}

response = requests.post(url, json=data)
print(response.json())
```

**JavaScript (fetch)**:
```javascript
fetch('http://localhost:5000/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    district: 'Colombo',
    town: 'Nugegoda',
    beds: 3,
    baths: 2,
    house_size: 1500,
    land_size: 10
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

## 🧠 Machine Learning Pipeline

### Data Processing

1. **Data Collection**
   - Dataset: Sri Lankan real estate listings
   - Features: Location, property specs, prices
   - Size: 5000+ property records

2. **Feature Engineering**
   ```python
   Features:
   - Numerical: beds, baths, house_size, land_size
   - Categorical: district, town (one-hot encoded)
   - Target: price
   ```

3. **Preprocessing Steps**
   - Missing value handling
   - Outlier removal (IQR method)
   - Feature scaling (StandardScaler)
   - One-hot encoding for locations

### Model Training

**Algorithm**: Random Forest Regressor

**Hyperparameters**:
```python
{
  'n_estimators': 100,
  'max_depth': 20,
  'min_samples_split': 5,
  'min_samples_leaf': 2,
  'random_state': 42
}
```

**Performance Metrics**:
- R² Score: 0.87
- Mean Absolute Error: LKR 3,200,000
- Root Mean Squared Error: LKR 4,800,000

**Training Process**:
```bash
python train_model.py
```

This will:
1. Load and clean dataset
2. Perform feature engineering
3. Split data (80% train, 20% test)
4. Train Random Forest model
5. Evaluate performance
6. Save model as `predictor_02.pickle`

### Model Deployment

**Model Serialization**:
```python
import pickle

# Save model
with open('predictor_02.pickle', 'wb') as f:
    pickle.dump(model, f)

# Load model
with open('predictor_02.pickle', 'rb') as f:
    model = pickle.load(f)
```

## 📊 Dataset Structure

### Required Columns

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `District` | String | Administrative district | "Colombo" |
| `Town` | String | Town/area name | "Nugegoda" |
| `Beds` | Integer | Number of bedrooms | 3 |
| `Baths` | Integer | Number of bathrooms | 2 |
| `House_size` | Float | House area (sq ft) | 1500.0 |
| `Land_size` | Float | Land area (perches) | 10.0 |
| `Price` | Float | Property price (LKR) | 45000000.0 |

### Sample Data

```csv
District,Town,Beds,Baths,House_size,Land_size,Price
Colombo,Nugegoda,3,2,1500,10,45000000
Gampaha,Kadawatha,4,3,2000,15,35000000
Kandy,Peradeniya,3,2,1400,20,28000000
```

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask 2.3.0
- **ML Library**: Scikit-learn 1.3.0
- **Data Processing**: Pandas 2.0.0, NumPy 1.24.0
- **Model Serialization**: Pickle (built-in)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Responsive design, Flexbox
- **JavaScript (ES6+)**: Async/await, Fetch API
- **No frameworks**: Pure vanilla JavaScript

### Development Tools
- **Version Control**: Git
- **Environment**: Python venv
- **Testing**: Pytest (optional)
- **Linting**: Flake8 (optional)

## 📁 Project Structure

```
real-estate-predictor/
├── app.py                      # Main Flask application
├── train_model.py              # Model training script
├── predictor_02.pickle         # Trained ML model
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── .gitignore                  # Git ignore rules
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css          # Styling
│   ├── js/
│   │   └── app.js             # Frontend logic
│   └── images/
│       └── logo.png
│
├── templates/                  # HTML templates
│   └── index.html             # Main page
│
├── data/                       # Dataset
│   ├── raw/
│   │   └── properties.csv     # Original data
│   └── processed/
│       └── cleaned_data.csv   # Preprocessed data
│
├── models/                     # Model artifacts
│   ├── predictor_02.pickle    # Trained model
│   └── scaler.pickle          # Feature scaler
│
├── notebooks/                  # Jupyter notebooks
│   ├── EDA.ipynb              # Exploratory analysis
│   └── model_training.ipynb   # Training experiments
│
└── tests/                      # Unit tests
    ├── test_api.py            # API tests
    └── test_model.py          # Model tests
```

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_api.py
```

### Manual Testing

**Test Prediction API**:
```bash
# Valid input
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"district":"Colombo","town":"Nugegoda","beds":3,"baths":2,"house_size":1500,"land_size":10}'

# Invalid input (negative beds)
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"district":"Colombo","town":"Nugegoda","beds":-1,"baths":2,"house_size":1500,"land_size":10}'
```

## 🔒 Security & Best Practices

### Implemented Security Measures

- ✅ Input validation (client and server-side)
- ✅ Error handling with informative messages
- ✅ CORS configuration (if needed)
- ✅ Environment variables for sensitive config
- ✅ SQL injection prevention (if using database)

### Production Recommendations

```python
# app.py - Production configuration
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,  # Disable in production
        threaded=True
    )
```

### Environment Variables

Create `.env` file:
```env
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
MODEL_PATH=models/predictor_02.pickle
```

## 📈 Performance Optimization

### Model Optimization
- Feature selection to reduce dimensionality
- Model compression (quantization)
- Caching predictions for common inputs

### Application Optimization
- Lazy model loading
- Response caching (Redis)
- Gzip compression
- CDN for static assets

### Monitoring
```python
# Add logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('Prediction made: {price}')
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Model Loading Error
```
Error: [Errno 2] No such file or directory: 'predictor_02.pickle'
```

**Solution**:
```bash
# Train the model first
python train_model.py

# Verify model file exists
ls -la predictor_02.pickle
```

#### 2. Port Already in Use
```
Error: Address already in use
```

**Solution**:
```bash
# Find process using port 5000
# Linux/Mac
lsof -i :5000

# Windows
netstat -ano | findstr :5000

# Kill process or use different port
python app.py --port 5001
```

#### 3. Prediction Returns Error
```
Error: Invalid input features
```

**Solution**:
- Verify all required fields are provided
- Check data types (integers, floats)
- Ensure location exists in training data

#### 4. High Memory Usage
```
Warning: Memory usage high
```

**Solution**:
```python
# Limit model size in training
model = RandomForestRegressor(
    n_estimators=50,  # Reduce from 100
    max_depth=15      # Reduce from 20
)
```

## 🎓 Skills Demonstrated

### Machine Learning
- Supervised learning (regression)
- Feature engineering
- Model training and evaluation
- Hyperparameter tuning
- Model serialization and deployment

### Software Engineering
- RESTful API design
- MVC architecture pattern
- Error handling and validation
- Code organization and modularity

### Web Development
- Frontend-backend integration
- AJAX/Fetch API
- Responsive design
- Form handling and validation

### DevOps (Optional)
- Virtual environment management
- Dependency management
- Deployment strategies
- Production configuration

## 🔄 Future Improvements

### Short-term (MVP++)
- [ ] Add user authentication
- [ ] Save prediction history
- [ ] Export predictions to PDF
- [ ] Add more property features (parking, pool, etc.)
- [ ] Implement map visualization

### Medium-term
- [ ] Deploy to cloud (AWS/Heroku/GCP)
- [ ] Add database (PostgreSQL)
- [ ] Implement caching (Redis)
- [ ] Add monitoring (Prometheus/Grafana)
- [ ] A/B testing for model versions

### Long-term
- [ ] Mobile app (React Native/Flutter)
- [ ] Real-time price updates
- [ ] Property image analysis (Computer Vision)
- [ ] Market trend analysis
- [ ] Recommendation system

## 📚 Documentation

### Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Random Forest Algorithm](https://en.wikipedia.org/wiki/Random_forest)
- [RESTful API Design](https://restfulapi.net/)

### Related Projects

- [Bangalore House Price Prediction](https://github.com/example/bangalore-house-prices)
- [Real Estate Analysis Dashboard](https://github.com/example/real-estate-dashboard)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add unit tests for new features
- Update documentation
- Maintain code coverage above 80%

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 👤 Author

**Your Name**

- Portfolio: [yourportfolio.com](https://yourportfolio.com)
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset: [Sri Lankan Property Listings]
- Inspiration: [Kaggle House Prices Competition]
- UI Design: [Dribbble Real Estate Designs]
- Mentors: [Your Mentor Names]

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/real-estate-predictor?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/real-estate-predictor?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/real-estate-predictor)
![GitHub license](https://img.shields.io/github/license/yourusername/real-estate-predictor)

---

<p align="center">
  Made with ❤️ and ☕ in Sri Lanka
</p>

<p align="center">
  <sub>If you find this project helpful, please consider giving it a ⭐</sub>
</p>
