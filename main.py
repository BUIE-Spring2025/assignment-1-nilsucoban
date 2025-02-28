def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    if not 1 <= num <= 3999:
        return None

    str_num = str(num)

    thousand_roman = []
    hundred_roman = []
    ten_roman = []
    unit_roman = []

    digit = len(str_num)
    
    final = ""
    
    def units_digit(unit):
        integer = int(unit)
        romanized = []
        if 9 > integer >= 5:
            romanized.append("V" + ("I" * (integer - 5)))
        elif integer == 9:
            romanized.append("IX")
        elif integer < 4 and not 0:
            romanized.append("I" * integer)
        elif integer == 4:
            romanized.append("IV")
        elif integer == 0:
            pass
        return romanized

    def tens_digit(tens):
        integer = int(tens)
        romanized = []
        if 9 > integer >= 5:
            romanized.append("L" + ("X" * (integer - 5)))
        elif integer == 9:
            romanized.append("XC")
        elif integer < 4 and not 0:
            romanized.append("X" * integer)
        elif integer == 4:
            romanized.append("XL")
        elif integer == 0:
            pass
        return romanized
        
    def hundredths_digit(hundredths):
        integer = int(hundredths)
        romanized = []
        if 9 > integer >= 5:
            romanized.append("D" + ("C" * (integer - 5)))
        elif integer == 9:
            romanized.append("CM")
        elif integer < 4 and not 0:
            romanized.append("C" * integer)
        elif integer == 4:
            romanized.append("CD")
        elif integer == 0:
            pass
        return romanized
        
    def thousands_digit(thousands):
        integer = int(thousands)
        romanized = []
        if integer < 4 and not 0:
            romanized.append("M" * integer)
        elif integer == 0:
            pass
        return romanized
        
    if int(digit) == 1:
        roman = units_digit(num)
    
    elif int(digit) == 2:
        unit_roman = units_digit(str_num[1])
        ten_roman = tens_digit(str_num[0])
        roman = ten_roman + unit_roman
    
    elif int(digit) == 3:
        unit_roman = units_digit(str_num[2])
        ten_roman = tens_digit(str_num[1])
        hundred_roman = hundredths_digit(str_num[0])
        roman = hundred_roman + ten_roman + unit_roman 
    
    elif int(digit) == 4:
        unit_roman = units_digit(str_num[3])
        ten_roman = tens_digit(str_num[2])
        hundred_roman = hundredths_digit(str_num[1])
        thousand_roman = thousands_digit(str_num[0])
        roman = thousand_roman + hundred_roman + ten_roman + unit_roman 

    for j in range(len(roman)):
        final += roman[j]

    return final

