#!/usr/bin/env python
# -*- coding: utf-8 -*-
file_names = ["BS.fna", "CWL.fna", "HI.fna", "LP.fna", "TE.fna"]

for i in file_names:
	file = open(i, 'r')
	len_tot = 0

	for p in file:
		if p[0] != ">":
			sequence = p[0:-1] # removes newline at end of line
			len_tot = len_tot + len(sequence)
		else:
			header = p
			print_header = header.replace("\n","")
	print "Genome in " + i + " has a length of " + str(len_tot)
