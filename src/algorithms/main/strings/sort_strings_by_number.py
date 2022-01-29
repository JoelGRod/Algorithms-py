"""
Natural sort

Your task is to sort a given string. Each word in the string will contain 
a single number. This number is the position the word should have in the 
result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the 
input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""
import re


def order(sentence):
  # code here
    my_list = sentence.split(" ")
    my_list.sort(key=natural_keys)
    return " ".join(my_list)


def natural_keys(text):
    return [int(c) for c in re.split(r'(\d+)', text) if c.isdigit()]
  

def order_extra(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
