import requests
r = requests.post("http://127.0.0.1:5000/predict",
                  json={"text":"A delivery attempt failed. Provide details here:"})
print(r.json())
