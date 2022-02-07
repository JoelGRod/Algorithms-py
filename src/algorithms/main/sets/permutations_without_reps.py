""" 
    Permutations without reps - no duplicates sol I
    O(n!)
    elements:
        string || char list || int list
"""

def permute_without_reps(elements):
    if len(elements) == 1:
        return elements

    permutation_opts = []

    recursive_permutations = permute_without_reps(elements[1:])

    first_opt = elements[0]

    for idx in range(len(recursive_permutations)):
        recursive_permutation = recursive_permutations[idx]

        for pos_idx in range(len(recursive_permutation) + 1):
            prefix = recursive_permutation[0: pos_idx]
            suffix = recursive_permutation[pos_idx:]
            permutation_opts.append(prefix + first_opt + suffix)

    return list(set(permutation_opts))

# Permutations no duplicates sol II - Slowest

def permute_without_reps_two(s):
    if len(s) == 1:
        return s
    else:
        return set(s[i]+p for i in range(len(s)) for p in permute_without_reps_two(s[:i] + s[i+1:]))


# Permutations no duplicates sol III

import itertools

def permute_without_reps_three(string):
    return {''.join(x) for x in itertools.permutations(string)}
