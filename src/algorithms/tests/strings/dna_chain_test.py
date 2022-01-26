import unittest
from algorithms.main.strings.dna_chain import DNA_strand

class TestDNAStrand(unittest.TestCase):
    def test_dna_strand(self):
        self.assertEqual(DNA_strand("AAAA"),"TTTT")
        self.assertEqual(DNA_strand("ATTGC"),"TAACG")
        self.assertEqual(DNA_strand("GTAT"),"CATA")


if __name__ == '__main__':
    unittest.main()