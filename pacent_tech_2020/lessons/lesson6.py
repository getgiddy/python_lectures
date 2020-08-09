
'''

70 > - Excellent
60 - 69 - Very Good
50 - 59 - Good
40 - 49 - Pass
39 < - Fail

'''

def check_result(score):
    if score >= 70 and score <= 100:
        print('Excellent')
    elif score >= 60 and score <= 69:
        print('Very Good')
    elif score >= 50 and score <= 59:
        print('Good')
    elif score >= 40 and score <= 49:
        print('Pass')
    elif score >= 0 and score <= 39:
        print('Fail')
    else:
        print('Invalid input')


check_result(24)