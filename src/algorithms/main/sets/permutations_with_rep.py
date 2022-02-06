"""
    Permutations with repetitions
    To find out a lock key...
    elements:
        string | chars list | int list
    O(n^r)
        r -> Number of slots to fill (permutation len)
"""


def permutations(elements, perm_len=None):
    if not perm_len:
        perm_len = len(elements)

    if perm_len == 1:
        return elements

    permutations_opt = []

    recursive_permutations = permutations(elements, perm_len - 1)

    for current in elements:
        for rec_permutation in recursive_permutations:
            permutations_opt.append(str(current) + str(rec_permutation))

    return permutations_opt
