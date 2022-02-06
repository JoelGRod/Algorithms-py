# Permutations no duplicates sol I


def permutations_no_rep(chars):
    if len(chars) == 1:
        return chars

    permutation_opts = []

    recursive_permutations = permutations_no_rep(chars[1:])

    first_opt = chars[0]

    for idx in range(len(recursive_permutations)):
        recursive_permutation = recursive_permutations[idx]

        for pos_idx in range(len(recursive_permutation) + 1):
            prefix = recursive_permutation[0: pos_idx]
            suffix = recursive_permutation[pos_idx:]
            permutation_opts.append(prefix + first_opt + suffix)

    return list(set(permutation_opts))

# Permutations no duplicates sol II - Slowest

def permutations_no_rep_two(s):
    if len(s) == 1:
        return s
    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations_no_rep_two(s[:i] + s[i+1:]))


# Permutations no duplicates sol III

import itertools

def permutations_no_rep_three(string):
    return {''.join(x) for x in itertools.permutations(string)}
