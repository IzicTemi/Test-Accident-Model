import pickle
from xml.sax.handler import feature_external_ges

from flask import Flask, request, jsonify

with open('model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

def transform(input):
    features = {}
    features['MONATSZAHL'] = input['Category']
    features['AUSPRAEGUNG'] = input['Type']
    features['JAHR'] = str(input['Year'])
    features['MONAT'] = str(input['Month'])
    return features

def predict(input):
    X = dv.transform(input)
    preds = model.predict(X)
    return float(preds[0])

app = Flask('accidents-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    input = request.get_json()

    features = transform(input)

    pred = predict(features)

    result = {
        "prediction": round(pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)