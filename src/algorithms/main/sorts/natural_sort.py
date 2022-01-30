"""
Natural Sort
Sort by specific part of the string (a number is the most common)

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


# import re

# def atoi(text):
#     return int(text) if text.isdigit() else text

# def natural_keys(text):
#     '''
#     alist.sort(key=natural_keys) sorts in human order
#     http://nedbatchelder.com/blog/200712/human_sorting.html
#     (See Toothy's implementation in the comments)
#     '''
#     return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# alist=[
#     "something1",
#     "something12",
#     "something17",
#     "something2",
#     "something25",
#     "something29"]

# alist.sort(key=natural_keys)
# print(alist)
