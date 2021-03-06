"""
    Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells 
    and carries the "instructions" for the development and functioning of 
    living organisms.
    
    If you want to know more: http://en.wikipedia.org/wiki/DNA
    
    In DNA strings, symbols "A" and "T" are complements of each other, as 
    "C" and "G". You function receives one side of the DNA (string, except 
    for Haskell); you need to return the other complementary side. DNA 
    strand is never empty or there is no DNA at all 
    (again, except for Haskell).
"""


def DNA_strand(dna):
    dna_comp = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    return "".join(list(map(lambda letter: dna_comp[letter], dna)))

#import string
def DNA_strand_extra(dna):
    # Python 2.7 solution
    #return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    return dna.translate(str.maketrans("ATCG","TAGC"))
