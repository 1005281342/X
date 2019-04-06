from sanic import Sanic
from sanic.response import json

from instance.instance import control

app = Sanic()


@app.route('/control', methods=['POST', 'GET'])
async def control_v1(req):
    num = int(dict(req.json).get('num'))
    res = control(num=num)
    return json(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6660)  # , workers=4
