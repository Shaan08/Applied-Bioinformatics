#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#files = ["BS.fna", "CWL.fna", "HI.fna", "LP.fna", "TE.fna"]
print sys.argv
def sequence_reader(file):
	""" Compiles the sequence of a file into a string"""
	sequence = ""
	for line in file:
		if line[0] != ">":
			seq_line = line[0:-1] # removes newline at end of line
			sequence = sequence + seq_line
	return sequence

def calc_GC_content(sequence):
	""" Count number of occurences of G and C in sequence-string"""
	G_content_absolute = sequence.count('G')
	C_content_absolute = sequence.count('C')
	GC_content_absolute = G_content_absolute + C_content_absolute
	# Here we ignore N, as opposed to the next assigment
	total_content = len(sequence)
	GC_content = float(GC_content_absolute)/float(total_content)
	return GC_content

#file_names = ["BS.fna", "CWL.fna", "HI.fna", "LP.fna", "TE.fna"]
basedir = "/Users/prashant/genomes/"
for i in sys.argv[1:]:
        file = open(basedir + i, 'r')
        print 

	sequence = sequence_reader(file)
	GC_content = calc_GC_content(sequence)
	print round(GC_content,4)
