def DNA_strand(dna):
    dna_comp = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    
    return "".join(list(map(lambda letter: dna_comp[letter], dna)))