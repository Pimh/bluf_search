from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
x = Seq("ATGAATGTGGTTTAGGTAG", generic_dna)
#import os
#os.chdir('/Users/PimH/Documents/Python_scripts')

def main():
    orfs = find_orfs(x)
    return orfs

# find ORFs within a given sequence and return their corresponding frame,ID,length, and location
def find_orfs(sequence):
                   
    
    norf = 0
    len_seq = len(sequence)
    orfs = []
                   
    for frame in range(0,3):
        i = frame
        find_start = True
        find_stop = False
        while i <= len_seq-3:
            print i
            while (i <= len_seq-3) & find_start:
                # check if the current codon is a start codon
                if str(sequence[i:i+3]) == 'ATG':
                   start = i
                   find_start = False
                   find_stop = True
                i = i +3
                   
            while (i <= len_seq-3) & find_stop:
                # check if the current codon is a stop codon
                if (str(sequence[i:i+3])=='TAA')|(str(sequence[i:i+3])=='TAG')|(str(sequence[i:i+3])=='TGA'):
                   stop = i
                   norf = norf + 1
                   find_start = True
                   find_stop = False
                   # return ORF sequence, length, and loction
                   orfs.append((norf,frame,sequence[start:stop],start,stop))
                i = i +3
            
            print 'norf', norf
            print 'frame', frame
                   
    return orfs
                   

               
