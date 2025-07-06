# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS # Required for cross-origin requests from frontend

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/')
def home():
    """
    A simple home route for the backend.
    """
    return "Welcome to the Pixel Health Backend API!"

@app.route('/calculate', methods=['POST'])
def calculate_health():
    """
    Calculates BMI, BMR, and TDEE based on provided user data.
    This endpoint demonstrates a backend calculation, though for BMI/BMR
    it's often done client-side.
    """
    data = request.get_json()

    # Extract data with default values or error handling
    gender = data.get('gender')
    weight = data.get('weight') # kg
    height = data.get('height') # cm
    age = data.get('age')
    activity_level = data.get('activityLevel')

    # Basic input validation
    if not all([gender, weight, height, age, activity_level]) or \
       not isinstance(weight, (int, float)) or weight <= 0 or \
       not isinstance(height, (int, float)) or height <= 0 or \
       not isinstance(age, int) or age <= 0:
        return jsonify({"error": "Invalid input. Please provide valid gender, positive weight, height, and age."}), 400

    # --- BMI Calculation ---
    height_in_meters = height / 100
    bmi = weight / (height_in_meters * height_in_meters)

    bmi_category = ''
    if bmi < 18.5:
        bmi_category = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        bmi_category = 'Normal weight'
    elif 25 <= bmi < 29.9:
        bmi_category = 'Overweight'
    else:
        bmi_category = 'Obesity'

    # --- BMR Calculation (Mifflin-St Jeor Equation) ---
    bmr = 0
    if gender == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 'female':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        return jsonify({"error": "Invalid gender. Must be 'male' or 'female'."}), 400

    # --- TDEE (Total Daily Energy Expenditure) Calculation ---
    activity_factor = 1.2 # Default to sedentary
    if activity_level == 'lightlyActive':
        activity_factor = 1.375
    elif activity_level == 'moderatelyActive':
        activity_factor = 1.55
    elif activity_level == 'veryActive':
        activity_factor = 1.725
    elif activity_level == 'superActive':
        activity_factor = 1.9

    tdee = bmr * activity_factor

    return jsonify({
        "bmi": round(bmi, 2),
        "bmiCategory": bmi_category,
        "bmr": round(bmr, 0),
        "tdee": round(tdee, 0)
    })

if __name__ == '__main__':
    # Run the Flask app on all available interfaces and port 5000
    app.run(host='0.0.0.0', port=5000)
