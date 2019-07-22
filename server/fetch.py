import requests
for i in range(100000):
    print(requests.get("http://127.0.0.1:8000/sentiment?sentence=你好嗎").text, i)
