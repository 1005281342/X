from sanic import Sanic
from sanic.response import json

from instance.instance import control

app = Sanic()


@app.route('/control')
async def control_v1(req):
    num = req.json.get('num')
    res = control(num=num)
    return json(res)
