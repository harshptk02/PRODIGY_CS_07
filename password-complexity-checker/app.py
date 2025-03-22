from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def assess_password_strength(password):
    strength_score = 0
    length_weight = 0.3
    uppercase_weight = 0.2
    lowercase_weight = 0.2
    number_weight = 0.2
    special_char_weight = 0.1
    
    feedback = []
    
    if len(password) >= 12:
        strength_score += length_weight
    else:
        feedback.append("Password should be at least 12 characters long.")
    
    if re.search(r'[A-Z]', password):
        strength_score += uppercase_weight
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    

    if re.search(r'[a-z]', password):
        strength_score += lowercase_weight
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
  
    if re.search(r'[0-9]', password):
        strength_score += number_weight
    else:
        feedback.append("Password should contain at least one number.")
    
   
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += special_char_weight
    else:
        feedback.append("Password should contain at least one special character.")
    

    if strength_score >= 0.9:
        strength_level = "Very Strong"
    elif strength_score >= 0.7:
        strength_level = "Strong"
    elif strength_score >= 0.5:
        strength_level = "Moderate"
    elif strength_score >= 0.3:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"
    

    if feedback:
        feedback_message = feedback
    else:
        feedback_message = ["Password meets all criteria."]
    
    return strength_level, feedback_message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form.get('password')
    strength_level, feedback_message = assess_password_strength(password)
    return jsonify({
        'strength_level': strength_level,
        'feedback_message': feedback_message
    })

if __name__ == '__main__':
    app.run(debug=True)