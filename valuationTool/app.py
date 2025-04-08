from flask import Flask, render_template, request, jsonify
import pickle
import hashlib

app = Flask(__name__)

# Load the trained model
try:
    with open('model/predictor_02.pickle', 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Model loading error: {e}")
    model = None

# Define validation ranges based on your dataset
VALIDATION_RANGES = {
    'Baths': {'min': 1, 'max': 10},  # Example: Baths should be between 1 and 10
    'Land_size': {'min': 1, 'max': 1000},  # Example: Land size should be between 1 and 1000 perches
    'Beds': {'min': 1, 'max': 10},  # Example: Beds should be between 1 and 10
    'House_size': {'min': 1, 'max': 10000}  # Example: House size should be between 1 and 10,000 sq.ft
}

# Define domain-specific validation rules
DOMAIN_RULES = {
    'House_size': {
        'min': 500,  # Minimum house size in sq.ft
        'max': 10000  # Maximum house size in sq.ft
    },
    'Land_size': {
        'min': 1,  # Minimum land size in perches
        'max': 1000  # Maximum land size in perches
    },
    'District': {
        'Mullativu': {
            'House_size': {'min': 500, 'max': 5000},  # Specific rules for Mullativu
            'Land_size': {'min': 5, 'max': 500}  # Specific rules for Mullativu
        },
        'Colombo': {
            'House_size': {'min': 800, 'max': 10000},  # Specific rules for Colombo
            'Land_size': {'min': 2, 'max': 1000}  # Specific rules for Colombo
        }
        # Add more districts as needed
    }
}

def validate_input(data):
    """Validate input data against predefined ranges and domain-specific rules."""
    errors = []
    for field, ranges in VALIDATION_RANGES.items():
        value = data.get(field)
        if value is None or not str(value).strip():
            errors.append(f"Missing {field}")
            continue

        try:
            value = float(value)
            if not (ranges['min'] <= value <= ranges['max']):
                errors.append(f"{field} must be between {ranges['min']} and {ranges['max']}")
        except ValueError:
            errors.append(f"{field} must be a valid number")

    # Domain-specific validation
    district = data.get('district')
    if district in DOMAIN_RULES['District']:
        district_rules = DOMAIN_RULES['District'][district]
        for field, rules in district_rules.items():
            value = data.get(field)
            if value is None or not str(value).strip():
                errors.append(f"Missing {field}")
                continue

            try:
                value = float(value)
                if not (rules['min'] <= value <= rules['max']):
                    errors.append(f"{field} for {district} must be between {rules['min']} and {rules['max']}")
            except ValueError:
                errors.append(f"{field} must be a valid number")

    return errors

def prepare_features(data):
    """Prepare features for prediction matching the model's training preprocessing"""
    try:
        # ===== 1. Numerical Features =====
        features = [
            float(data['Baths']),
            float(data['Land_size']),
            float(data['Beds']),
            float(data['House_size'])
        ]

        # ===== 2. District One-Hot Encoding (24 districts) =====
        districts = [
            'Ampara', 'Anuradhapura', 'Badulla', 'Batticaloa', 'Colombo',
            'Galle', 'Gampaha', 'Hambantota', 'Jaffna', 'Kalutara',
            'Kandy', 'Kegalle', 'Kurunegala', 'Mannar', 'Matale',
            'Matara', 'Monaragala', 'Mullativu', 'Nuwara Eliya',
            'Polonnaruwa', 'Puttalam', 'Ratnapura', 'Trincomalee', 'Vavuniya'
        ]
        district = data['district']
        for d in districts:
            features.append(1 if d == district else 0)

        # ===== 3. Town Encoding (219 features) =====
        # Consistent with training preprocessing
        town = data['town'].strip().encode('utf-8')
        town_hash = int(hashlib.sha256(town).hexdigest(), 16) % 219
        town_features = [0] * 219
        town_features[town_hash] = 1
        features += town_features

        if len(features) != 247:
            raise ValueError(f"Feature count mismatch: {len(features)} features created")
        
        print(f"🛠️ Prepared {len(features)} features")
        return features
    except Exception as e:
        print(f"❌ Feature preparation error: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.get_json()
        print("📩 Received data:", data)

        # Validate required fields and input ranges
        required_fields = ['Baths', 'Land_size', 'Beds', 'House_size', 'district', 'town']
        for field in required_fields:
            if field not in data or not str(data[field]).strip():
                return jsonify({'error': f'Missing {field}'}), 400

        # Validate numerical fields and domain-specific rules
        validation_errors = validate_input(data)
        if validation_errors:
            return jsonify({'error': 'Validation failed', 'details': validation_errors}), 400

        # Prepare features
        features = prepare_features(data)
        if not features:
            return jsonify({'error': 'Feature preparation failed'}), 400

        # Predict
        prediction = model.predict([features])
        predicted_price = round(prediction[0], 2)

        return jsonify({'predicted_price': predicted_price})

    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)