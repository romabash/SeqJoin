# SeqJoin
### A pipeline to process and analyze Sanger sequencing data
- Perform quality trimming
- Reverse complement of the reverse sequence
- Align and join the two reads together 
- Translate the DNA sequence into protein sequence
- Save and retrieve files

#### Written in Python2.7 and Biopython

### Example:

> Import SeqJoin and Biopython:
```python
from SeqJoin import SeqJoin
from Bio import SeqIO
```

> Provide the names of the forward and reverse sequence files:
```python
#sequence files to join together (example forward and reverse sequence files)
files = ['seq1.seq', 'seq1-1.seq']
```

>Provide primers to check if sequence file contains the right sequence:
```python
forward_primer = "ATGC" #example primers
reverse_primer = "CGTA" #example primers
```
>Run SeqJoin with given parameters
```python
sample = SeqJoin(files, forward_primer, reverse_primer)
```
>Get forward and reverse sequences if primers match
```python
print(sample.forward_seq())
print(sample.reverse_seq())
```
>If both primers match, makes a SeqRecord for DNA sequence
```python
dna_seq = sample.dna_seq()
print(dna_seq.format('fasta'))
```
>Translates DNA SeqRecord into Protein SeqRecord
```python
protein_seq = sample.protein_seq()
print(protein_seq.format('fasta'))
```
>Save 
```python
sample.save(dna_seq, "dna_data.fasta")
sample.save(protein_seq, "protein_data.fasta")
```   
>Retrieve certain DNA sequence using file ID (based on the name of the original sequence file name)
```python
pick_dna = sample.retrieve('dna_data.fasta', 'seq1')
print(pick_dna)
```
>Retrieve certain protein sequence using file ID (based on the name of theoriginal sequence file name)
```python
pick_protein = sample.retrieve('protein_data.fasta', 'seq1')
print(pick_protein)
```

