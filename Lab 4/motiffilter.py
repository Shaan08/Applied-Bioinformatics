#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import re
import sys

try:
        file_name =  sys.argv[1]
except:
        sys.exit("Error: You have to specify input FASTA-file!")

def find_motif(sequence):
	sequence = str(sequence)
	res = bool(re.search('KL[EI]{2,}K', str(sequence)))
	if res is True:
		return True	
	
sequence_count = 0

try:
        file_name =  sys.argv[1]
except:
        sys.exit("Error: You have to specify input FASTA-file!")

for seq_record in SeqIO.parse(file_name, "fasta"):
	sequence = seq_record.seq
	if find_motif(sequence) is True:
		print seq_record.format("fasta")
		sequence_count += 1
print "There are " + str(sequence_count) + " \"KLEEK\" proteins in the test data"
