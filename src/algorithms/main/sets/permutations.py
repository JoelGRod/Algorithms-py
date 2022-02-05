# Unfinished - TODO

def permutations_no_reps(string):
    #your code here
    chars = list(string)
    if len(chars) == 1: return chars

    permutation_opts = []

    recursive_permutations = permutations_no_reps("".join(chars[1:]))
    
    first_opt = chars[0]
    
    for idx, char in enumerate(recursive_permutations):
        recursive_permutations = recursive_permutations[idx]
        
        for pos_idx, rec_char in enumerate(recursive_permutations):
            prefix = recursive_permutations[0: pos_idx]
            suffix = recursive_permutations[pos_idx]
            permutation_opts.append(prefix + first_opt + suffix)
    
    return permutation_opts