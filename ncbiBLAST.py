from Bio.Blast import NCBIWWW

query ='LVSCCYRSLAAPDLTLRDLLDIVETSQAHNARAQLTGALFYSQGVFFQWLEGRPAAVAEVMTHIQRDRRHSNVEILAEEPIAKRRFAGWHMQ'
result_handle = NCBIWWW.qblast("blastp", "nr", query)
save_file = open("my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
