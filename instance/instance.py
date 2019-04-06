from utils.constant import Rule
from core.service import Control


def control(num: int):
    C = Control()
    num = int(num)
    print(num)
    if num in {Rule['OPEN_LED'], Rule['OPEN_FAN']}:
        print(Rule[num])
        C.open(num=Rule[num])
        return {'status': 'open'}
    elif num in {Rule['CLOSE_LED'], Rule['CLOSE_FAN']}:
        print(Rule[num])
        C.close(num=Rule[num])
        return {'status': 'close'}
    elif num == Rule['OK']:
        C.set_output(C.led_bcm)
        C.set_output(C.fan_bcm)
        return {'status': 'init'}
