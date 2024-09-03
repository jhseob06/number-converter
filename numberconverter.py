numbers = {
    '일' : 1,
    '하나' : 1,
    '둘' : 2,
    '이' : 2,
    '셋' : 3,
    '삼' : 3,
    '사' : 4,
    '넷' : 4,
    '다섯' : 5,
    '오' : 5,
    '육' : 6,
    '여섯' : 6,
    '일곱' : 7,
    '칠' : 7,
    '여덟' : 8,
    '여덜' : 8,
    '팔' : 8,
    '아홉' : 9,
    '구' : 9,
    '십' : 10,
    '열' : 10,
    '이십' : 20,
    '스물' : 20,
    '서른' : 30,
    '삼십' : 30,
    '마흔' : 40,
    '사십' : 40,
    '쉰' : 50,
    '오십' : 50,
    '예순' : 60,
    '육십' : 60,
    '일흔' : 70,
    '칠십' : 70,
    '팔십' : 80,
    '여든' : 80,
    '아흔' : 90,
    '구십' : 90
}

def number_exper(value):
    num=0

    while len(value)>0:
        if len(value) > 2:
            if value.startswith('쉰'):
                num+=50
                value = value[1:]
            elif value.startswith('십') or value.startswith('열'):
                num+=10
                value = value[1:]
            else:
                num+=numbers[value[:2]]
                value = value[2:] 
        elif len(value)==2:
            if value.startswith('십') or value.startswith('열'):
                num+=10
                value = value[1:]
            elif value.startswith('쉰'):
                num+=50
                value = value[1:]
            else:
                num+=numbers[value]
                value = value[2:]
        else:
            num+=numbers[value]
            value = value[1:]

    return num

try:
    while True:
        value = input('입력: ')
        try:
            print(number_exper(value))
        except:
            print('올바르지 않은 입력')
except KeyboardInterrupt:
    print('stop')

