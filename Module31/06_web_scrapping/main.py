# TODO здесь писать код
import requests
import json

if __name__ == "__main__":
    req = requests.get('http://www.columbia.edu/~fdc/sample.html')

    data = json.loads(req.text)
    print(data)
    with open('test.json', 'w', encoding="UTF8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
