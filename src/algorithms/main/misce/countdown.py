""" Countdown
"""

def count_down(value):
    print(value)
    if value <= 0: return           # Base Case
    else: count_down(value - 1)     # Recursive case

print("Countdown\n", "-----------------------")
count_down(10)