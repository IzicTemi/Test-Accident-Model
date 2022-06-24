import pickle

from flask import Flask, request, jsonify

with open('model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

def predict(input):
    X = dv.transform(input)
    preds = model.predict(X)
    return float(preds[0])

app = Flask('accidents-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    input = request.get_json()

    pred = predict(input)

    result = {
        "prediction": pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')