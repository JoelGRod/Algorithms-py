class RomanNumerals:

    roman_rosetta = {
        "I":    1,
        "IV":   4,
        "V":    5,
        "X":    10,
        "L":    50,
        "C":    100,
        "D":    500,
        "M":    1000
    }

    @classmethod
    def to_roman(cls, val):
        result = ""
        str_val = str(val)
        values = [digit + "0" * (len(str_val) - (idx + 1))
                  for idx, digit in enumerate(str_val)
                  if digit != "0"]

        for digit in values:
            if len(digit) == 4:
                val = int(digit) / 1000
                result += ("M" * int(val))
            if len(digit) == 3:
                val = int(digit) / 100
                if val < 4:
                    result += ("C" * int(val))
                if 4 < val < 9:
                    result += "D" + "C" * (int(val) - 5)
                if val == 4:
                    result += "CD"
                if val == 9:
                    result += "CM"
            if len(digit) == 2:
                val = int(digit) / 10
                if val < 4:
                    result += ("X" * int(val))
                if 4 < val < 9:
                    result += "L" + "X" * (int(val) - 5)
                if val == 4:
                    result += "XL"
                if val == 9:
                    result += "XC"
            if len(digit) == 1:
                val = int(digit)
                if val < 4:
                    result += ("I" * int(val))
                if 4 < val < 9:
                    result += "V" + "I" * (int(val) - 5)
                if val == 4:
                    result += "IV"
                if val == 9:
                    result += "IX"

        return result

    @classmethod
    def from_roman(cls, roman_num):
        result = 0
        for idx, r_digit in enumerate(roman_num):
            if ((idx) == len(roman_num) - 1 or
                    cls.roman_rosetta[r_digit] >= cls.roman_rosetta[roman_num[idx + 1]]):
                result += cls.roman_rosetta[r_digit]
            else:
                result -= cls.roman_rosetta[r_digit]
        return result


# Solution II
class RomanNumeralsTwo:

    ROMANS = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'C': 100,
        'XC': 90,
        'L': 50,
        'X': 10,
        'V': 5,
        'IV': 4,
        'I': 1,
    }

    @classmethod
    def to_roman(cls, n):
        s = ''
        for key, value in cls.ROMANS.items():
            while n % value != n:
                n = n - value
                s += key
        return s

    @classmethod
    def from_roman(cls, r):
        s = 0
        for key, value in cls.ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s


# Solution III
from collections import OrderedDict
import re

class RomanNumeralsThree(object):

    ROMAN_NUMERALS = OrderedDict([
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1),
    ])

    DECIMAL_TO_ROMAN = [(v, k) for k, v in ROMAN_NUMERALS.items()]

    ROMAN_RE = '|'.join(ROMAN_NUMERALS)
    
    @classmethod
    def from_roman(cls, roman):
        return sum(cls.ROMAN_NUMERALS[d] for d in re.findall(cls.ROMAN_RE, roman))

    @classmethod
    def to_roman(cls, decimal):
        result = []
        for number, roman in cls.DECIMAL_TO_ROMAN:
            while decimal >= number:
                decimal -= number
                result.append(roman)
        return ''.join(result)