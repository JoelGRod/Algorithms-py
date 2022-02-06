"""
    Permutations with repetitions
    To find out a lock key...
    O(n^r)
        r -> Number of slots to fill (permutation len)
"""


def permutations(chars, perm_len=None):
    if not perm_len:
        perm_len = len(chars)

    if perm_len == 1:
        return chars

    permutations_opt = []

    recursive_permutations = permutations(chars, perm_len - 1)

    for current in chars:
        for rec_permutation in recursive_permutations:
            permutations_opt.append(str(current) + str(rec_permutation))

    return permutations_opt
