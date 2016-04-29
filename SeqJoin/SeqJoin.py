from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC, generic_dna
from Bio.SeqRecord import SeqRecord
import pickle
import os.path
import sys

class SeqJoin(object):
    
    def __init__(self, files, foward_primer, reverse_primer):

        self.files = files
        self.foward_primer = foward_primer
        self.reverse_primer = reverse_primer
        for f in self.files:
            if not os.path.isfile(f):
                print "There is no such file as %s" %f
                sys.exit(1) #ends script if either file is not in the directory

    def foward_seq(self):
    #reads file and returns foward sequence
        
        for x, seq_file in enumerate(self.files):
            with open(seq_file, 'r') as f:
                sequence = f.read()
                sequence = "".join(sequence.split())

            if self.foward_primer in sequence:
                start = sequence.index(self.foward_primer)   
                end = sequence[start:].index('N')
                foward_seq = Seq(sequence[start:(end-20)], generic_dna)
                return foward_seq

    def reverse_seq(self):
    #reads file and returns reverse sequence

        for x, seq_file in enumerate(self.files):
            with open(seq_file, 'r') as f:
                sequence = f.read()
                sequence = "".join(sequence.split())

            if self.reverse_primer in sequence:
                start = sequence.index(self.reverse_primer)   
                end = sequence[start:].index('N')
                reverse_seq = Seq(sequence[start:(end-20)], generic_dna)
                reverse_seq_comp = reverse_seq.reverse_complement()
                reverse_seq = Seq(str(reverse_seq_comp), generic_dna)
                return reverse_seq

    def long_substr(self, data):
    #returns the longest substring between two strings
    
        substr = ''
        if len(data) > 1 and len(data[0]) > 0:
            for i in range(len(data[0])):
                for j in range(len(data[0])-i+1):
                    if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                        substr = data[0][i:i+j]
        return substr

    def dna_seq(self):
    #if foward and reverse sequence exist, returns full sequence joined together as Biopython SeqRecord
    #returns "NO MATCH" if both or one of the sequences doesn't exist

        a = str(self.foward_seq())
        b = str(self.reverse_seq())

        if a != "None" and b != "None":   
            common = self.long_substr([a, b])

            seq = Seq(a[0:a.index(common)] + b[b.index(common):], generic_dna)

            dna_record = SeqRecord(seq)
            dna_record.id = '%s' %self.files[0][:self.files[0].find('.')]
            dna_record.name = '' 
            dna_record.description = '%s Nucleotide Bases' %len(dna_record)

            return dna_record
            
        else:
            return "NO MATCH"

    def protein_seq(self):
    #if SeqRecord exist, returns protein sequence as Biopython SeqRecord
    #returns "NO MATCH" if both or one of the sequences doesn't exist
        seq_record = self.dna_seq()
        
        if seq_record == "NO MATCH":
            return "NO MATCH"
        else:
            protein = seq_record.seq.translate()
            protein_record = SeqRecord(protein)
            protein_record.id = '%s' %self.files[0][:self.files[0].find('.')]
            protein_record.name = '' 
            protein_record.description = '%s Amino Acids' %len(protein_record)

            return protein_record

    def save(self, seq_record, file_name):
    #Saves SeqRecords (protein or DNA) in a file and as a pickle to access individual SeqRecords later

        if seq_record == "NO MATCH":
            print "NO SEQUENCE TO SAVE"
        else:
            array = []
            array.append(seq_record)
            data = SeqIO.to_dict(array) #using record id as a key

            #storing all results in a pickle to access later
            all_data = {}
            try:
                pickle_handle = file_name[:file_name.find('.')]+'.pickle'
                look = open(pickle_handle, 'rb')
                all_data = pickle.load(look)
                all_data.update(data)

                records = all_data.values()
                SeqIO.write(records, file_name, "fasta")

                store = open(pickle_handle, 'wb')
                pickle.dump(all_data, store)
                store.close()

            except Exception as e:
                all_data.update(data)

                records = all_data.values()
                SeqIO.write(records, file_name, "fasta")
        
                pickle_handle = file_name[:file_name.find('.')]+'.pickle'
                store = open(pickle_handle, 'wb')
                pickle.dump(all_data, store)
                store.close()

    def retrieve(self, file_name, name):
    #Retrieves individual SeqRecord from a pickle associated with the its file
    
        try:
            item = {}
            pickle_handle = file_name[:file_name.find('.')]+'.pickle'
            look = open(pickle_handle, 'rb')
            item = pickle.load(look)
            return item.get(name, "No such record: %s" %name)
        except IOError as e:
            print "Invalid file name: %s" %file_name

        
        
   



