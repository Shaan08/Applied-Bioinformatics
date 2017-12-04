#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Bio import SeqIO
import sys

try:
	file_name =  sys.argv[1]
except:
        sys.exit("Error: You have to specify input FASTA-file!")

for seq_record in SeqIO.parse(file_name, "fasta"):
	print ">" + seq_record.id
	DNA = seq_record.seq
	print DNA.translate()
