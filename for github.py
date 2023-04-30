def int_to_roman(num: int) -> str:
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_numeral = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while value <= num:
            roman_numeral += numeral
            num -= value
    return roman_numeral


print(int_to_roman(11))


def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for i in s[::-1]:
        curr = roman_dict[i]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result


print(roman_to_int('XI'))
