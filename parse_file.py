from Bio import SeqIO

def main():
    sequences = parse_file(filename)
    nseq = len(sequences)
    
    for seq in sequences:
        orfs = find_orfs(seq.sequence)


def parse_file(filename):
    # read FASTA file and parse into separate sequences
    handle = open("/Users/PimH/Documents/Research_Chow_lab/Insect_db/1kite_species_103_species/110817_I809_FCD05CDACXX_L3_INSbusTBCRABPEI-135_e1.scafseq_200","rU")

    # convert sequence iterator into records list
    records = list(SeqIO.parse(handle,"fasta"))
    return records
               

# find ORFs within a given sequence and return their corresponding frame,ID,length, and location
def find_orfs(sequence):
                   
    
    norf = 0
    len_seq = len(sequence)
    orfs = []
                   
    for frame in range(0,3):
        i = frame
        find_start = True
        find_stop = False
        while i < len_seq-3:
            while (i <= len_seq-3) & find_start:
                # check if the current codon is a start codon
                if str(sequence[i:i+2]) == 'ATG':
                   start = i
                   find_start = False
                   find_stop = True
                i = i +3
                   
            while (i <= len_seq-3) & find_stop:
                # check if the current codon is a stop codon
                if (str(sequence[i:i+2])=='TAA')|(str(sequence[i:i+2])=='TAG')|(str(sequence[i:i+2])=='TGA'):
                   stop = i
                   norf = norf + 1
                   find_start = True
                   find_stop = False
                   # return ORF sequence, length, and loction
                   orfs.append((norf,frame,sequence[start:stop],start,stop))
                i = i +3
                   
    return orfs
                   

               
                   
# blast a reference bluf domain against the ORFs and return the hits with blast stats
def bluf_blast(sbj_seq,ORFs):


