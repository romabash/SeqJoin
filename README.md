# SeqJoin
###SeqJoin joins two sequencing files taken from forward and reverse primers together

###Written in Python2.7 and Biopython

##Example:

> Import SeqJoin and Biopython:
```python
from SeqJoin import SeqJoin
from Bio import SeqIO
```

> Provide the names of the forward and reverse sequence files and both primers:
```python
#sequence files to join together (example forward and reverse sequence files)
files = ['seq1.seq', 'seq1-1.seq']

#primers to check if sequence file contains the right sequence
forward_primer = "ATGC" #example primers
reverse_primer = "CGTA" #example primers

#run SeqJoin with given parameters
sample = SeqJoin(files, forward_primer, reverse_primer)

#prints forward and reverse sequences if primers match
print sample.forward_seq()
print sample.reverse_seq()

#if both primers match, makes a SeqRecord for DNA sequence
dna_seq = sample.dna_seq()
print dna_seq.format('fasta')
print '\n'

#translates DNA SeqRecord into protein SeqRecord
protein_seq = sample.protein_seq()
print protein_seq.format('fasta')
print '\n'

#promts to save
answer = raw_input("Do you want to save this sequence? \n> ")
if answer.lower() == "yes" or answer.lower() == "y":
    sample.save(dna_seq, "dna_data.fasta")
    sample.save(protein_seq, "protein_data.fasta")

#Retrieve certain DNA sequence using file ID (based on the name of theoriginal sequence file name)
pick_dna = sample.retrieve('dna_data.fasta', 'seq1')
print pick_dna

#Retrieve certain protein sequence using file ID (based on the name of theoriginal sequence file name)
pick_protein = sample.retrieve('protein_data.fasta', 'seq1')
print pick_protein
```
