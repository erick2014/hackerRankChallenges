# https://www.hackerrank.com/challenges/the-time-in-words/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def getTimeInLetters(hour):
    return {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eigth',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourtheen',
        15: 'fiftheen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twenty four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eigth',
        29: 'twenty nine',
        30: 'thirty',
        31: 'thirty one',
        32: 'thirty two',
        32: 'thirty two',
        33: 'thirty three',
        34: 'thirty four',
        35: 'thirty five',
        36: 'thirty six',
        37: 'thirty seven',
        38: 'thirty eigth',
        39: 'thirty nine',
        40: 'forty',
        41: 'forty one',
        42: 'forty two',
        43: 'forty three',
        44: 'forty four',
        45: 'forty five',
        46: 'forty six',
        47: 'forty seven',
        48: 'forty eigth',
        49: 'forty nine',
        50: 'fifty',
        51: 'fifty one',
        52: 'fifty two',
        53: 'fifty three',
        54: 'fifty four',
        55: 'fifty five',
        56: 'fifty six',
        57: 'fifty seven',
        58: 'fifty eigth',
        59: 'fifty nine',
        60: 'sixty',
    }[hour]


def getMinutesMessage(minutes):
    if minutes == 1:
        return 'minute'
    else:
        return 'minutes'


def timeInWords(h, m):
    if m == 0 or m == '00':
        return getTimeInLetters(h)+" o' clock"
    elif m == 15:
        return "quarter past "+getTimeInLetters(h)
    elif m == 30:
        return "half past "+getTimeInLetters(h)
    elif m == 45:
        return "quarter to "+getTimeInLetters(h+1)
    elif m > 0 and m < 40:
        return getTimeInLetters(m) + ' ' + getMinutesMessage(m) + ' past '+getTimeInLetters(h)
    elif m >= 40:
        minutesRemaining = 60 - m
        return getTimeInLetters(minutesRemaining) + ' ' + getMinutesMessage(m) + ' to ' + getTimeInLetters(h+1)


h = int(input())
m = int(input())
result = timeInWords(h, m)
print(result)
