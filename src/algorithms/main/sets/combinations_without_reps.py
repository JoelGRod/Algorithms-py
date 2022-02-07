"""
This is how lotteries work. The numbers are drawn one at a time, 
and if we have the lucky numbers (no matter what order) we win!

No Repetition: such as lottery numbers (2,14,15,27,30,33)

Number of combinations:
n! / r!(n - r)! = (n r)

Where n is the number of things to choose from, 
and we choose r of them, no repetition, order doesn't matter.

It is often called "n choose r" (such as "16 choose 3"). 
And is also known as the Binomial Coefficient.
"""

def combine_without_reps(options, comb_len):
    if comb_len == 1: return options
    
    combos = []

    for idx, option in enumerate(options):
        recursive_combos = combine_without_reps(options[idx + 1:], comb_len - 1)

        for recursive_combo in recursive_combos:
            combos.append(str(option) + str(recursive_combo))
    
    return combos
