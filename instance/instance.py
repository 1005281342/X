from utils.constant import Rule
from core.service import Control


def control(num: int):
    C = Control()

    if num in {Rule['OPEN_LED', 'OPEN_FAN']}:
        C.open(num=num)
        return {'status': 'open'}
    elif num in {Rule['CLOSE_LED'], Rule['CLOSE_FAN']}:
        C.close(num=num)
        return {'status': 'close'}
    elif num == Rule['OK']:
        C.set_output(C.led_bcm)
        C.set_output(C.fan_bcm)
