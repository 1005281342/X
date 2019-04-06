import json
import requests

from utils.constant import URL, DATA


def post(url=URL, data=DATA):
    res = requests.post(url=url, data=json.dumps(data),
                        headers={'Content-Type': 'application/json'})
    return res.json()


if __name__ == '__main__':
    print(post('http://192.168.43.85:6660/control',
               {
                   "num": 5
               }
               ))
