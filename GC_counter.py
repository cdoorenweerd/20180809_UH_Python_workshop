from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)

print("Total length of the sequence:")
print(len(my_seq))

print("Number of G's:")
print(my_seq.count("G"))

print("GC percentage:")
print(GC(my_seq))