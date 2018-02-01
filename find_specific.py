from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
from Bio import SeqIO

handle=open("/Users/PimH/Documents/Research_Chow_lab/Insect_db/1kite_species_103_species/120215_I277_FCD0KP1ACXX_L1_INSfrgTBBRAAPEI-56_e1.scafseq_200")

records=list(SeqIO.parse(handle,"fasta"))

for i in range(1,len(records)):
	if str(records[i].id)=='C404613':
		protein=records[i].seq[2:].translate()
		print “i:”,i
		print protein
		

