import requests

input = {
    "Category": 'Alkoholunfälle',
    "Type": 'insgesamt',
    "Year": '2021',
    "Month": '01'
}

url = 'http://localhost:5000/predict'
response = requests.post(url, json=input)
print(response.json())