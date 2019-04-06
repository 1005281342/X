URL = 'http://192.168.43.85:6660/control'
DATA = {'num': 1}

Rule = {
    'OPEN_LED': 1,
    'CLOSE_LED': 5,
    'OPEN_FAN': 4,
    'CLOSE_FAN': 2,
    'OK': 3,

    1: 26,
    5: 26,
    4: 18,
    2: 18,
}

NumMap = {
    'ZERO': 0,
    'ONE': 1,
    'TWO': 2,
    'THREE': 3,
    'FOUR': 4,
    'FIVE': 5
}

if __name__ == '__main__':
    num = 5
    print(Rule.get(num))
