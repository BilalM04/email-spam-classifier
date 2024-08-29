from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load your trained model and the feature extractor (vectorizer)
with open('models/spam_classifier_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/feature_extractor.pkl', 'rb') as extractor_file:
    feature_extraction = pickle.load(extractor_file)

@app.route('/predict', methods=['GET'])
def predict():
    # Get the message from the request
    input_mail = [request.args.get('message')]

    # Transform the message using the feature extraction method
    input_mail_features = feature_extraction.transform(input_mail)

    # Make the prediction
    prediction = model.predict(input_mail_features)

    # Interpret the result
    result = 'not spam' if prediction[0] == 0 else 'spam'

    return jsonify({
        'message': input_mail[0],
        'prediction': result
    })

if __name__ == '__main__':
    app.run(debug=True)
