import re

lower = 372304
upper = 847060


def check_same_increase(number):
    num = str(number)
    for i in range(5):
        if int(num[i + 1]) < int(num[i]):
            return False
    return True


def check_doubles(number):
    num = str(number)
    matches = re.findall('44+|55+|66+|77+|88+|99+', num)
    if matches and min([len(match) for match in matches]) == 2:
        return True
    else:
        return False


check_increasing_list = [num for num in range(lower, upper + 1) if check_same_increase(num)]
double_check_list = [num for num in check_increasing_list if check_doubles(num)]

print(len(double_check_list))
