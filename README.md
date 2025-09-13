Phishing Email Detection System

*A simple and efficient machine learning project to detect whether an email is phishing or legitimate. 
*This system uses TF-IDF vectorization and a Logistic Regression classifier and provides a Flask API for real-time predictions.

Overview
*The Phishing Email Detection System helps users automatically identify phishing emails, preventing potential scams. 
*The project works entirely locally and provides an easy-to-use API for instant predictions.

How it works ?
1.Email text is converted into numerical features using TF-IDF.
2.A Logistic Regression model predicts whether the email is phishing or legitimate.
3.Users can send emails to a Flask API and receive predictions immediately.

Key Features
*Real-time email classification via API.
*Lightweight and easy to run locally.
*Reusable trained model and vectorizer.
*Easily extensible with more data or advanced models.

Final Command of Execution
# 1. Install dependencie
pip install -r requirements.txt
# 2. Train model
python train_model.py
# 3. Run API
python app.py
# 4. Test API
python test_request.py
