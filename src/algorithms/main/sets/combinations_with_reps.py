"""
Repetition is Allowed: such as coins in your pocket (5,5,5,10,10)

Or let us say there are five flavours of ice cream: 
banana, chocolate, lemon, strawberry and vanilla.

We can have three scoops. How many variations will there be?

Let's use letters for the flavours: {b, c, l, s, v}. 
Example selections include:
    {c, c, c} (3 scoops of chocolate)
    {b, l, v} (one each of banana, lemon and vanilla)
    {b, v, v} (one of banana, two of vanilla)

Number of combinations:
(r + n - 1    r) = (r + n - 1)! / r!(n - 1)!

Where n is the number of things to choose from, and we 
choose r of them. Repetition allowed, order doesn't matter.
"""

def combine_with_reps(options, comb_len):
    pass