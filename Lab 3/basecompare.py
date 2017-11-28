#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
def sequence_reader(file):
        """ Compiles the sequence of a file into a string"""
        sequence = ""
        for line in file:
                if line[0] != ">":
                        seq_line = line[0:-1] # removes newline at end of line
                        sequence = sequence + seq_line
        else:
            acc_nm = line
        return sequence, acc_nm

def calc_comp_vector(sequence):
    A_content_absolute = float(sequence.count('A'))
    C_content_absolute = float(sequence.count('C'))
    G_content_absolute = float(sequence.count('G'))
    T_content_absolute = float(sequence.count('T'))

    total_content = A_content_absolute + C_content_absolute + G_content_absolute + T_content_absolute
    A_content = A_content_absolute/total_content
    C_content = C_content_absolute/total_content
    G_content = G_content_absolute/total_content
    T_content = T_content_absolute/total_content
    comp_vector = [A_content,C_content,G_content,T_content]
    return comp_vector

def calc_dist(comp_vector1,comp_vector2):
    cp1 = comp_vector1
    cp2 = comp_vector2

    d0 = cp1[0] - cp2[0]
    d1 = cp1[1] - cp2[1]
    d2 = cp1[2] - cp2[2]
    d3 = cp1[3] - cp2[3]
    dist_squared = d0**2 + d1**2 + d2**2 + d3**2
    diff_in_comp_vector = math.sqrt(dist_squared)/2
    return diff_in_comp_vector
def generate_distance_matrix(acc_nm_list,comp_vectors):
    len_comp_vector = len(comp_vectors)
    matrix = [[0 for x in xrange(len_comp_vector)] for y in xrange(len_comp_vector)] 
    print acc_nm_list
    # Fill index
    for i in range(1,len_comp_vector):
        matrix[0][i] = comp_vectors[i]
        matrix[i][0] = comp_vectors[i]

    #print comp_vectors
    
    for i in range(0,len_comp_vector):
        for p in range(0,len_comp_vector):
            comp_vector1 = comp_vectors[i]
            comp_vector2 = comp_vectors[p]
            distance = calc_dist(comp_vector1,comp_vector2)
            matrix[i][p] = distance     
        distance_matrix = matrix
    return distance_matrix

def Phylip_format_matrix(acc_nm_list,distance_matrix):
    line = ""
    print len(acc_nm_list)
    for i in range(0,len(acc_nm_list)):
        acc_number = acc_nm_list[i]
        # acc number formatting
        acc_number = acc_number[1:11]
        acc_number = acc_number.split(' ')[0]
        acc_number = acc_number + " " * (10-len(acc_number))
#       acc_number = acc_number.replace('>','')
        line = acc_number
        for p in distance_matrix[i]:
            line = line + str(round(p,3)) + "\t"
        #print line

#file_names = ["human.fa" "mouse.fa" "fly.fa" "yeast.fa" "ecoli.fa" "plasmodium.fa" "thermus.fa"]
basedir = "/Users/prashant/data/"
comp_vectors = []
acc_nm_list = []
for i in sys.argv[1:]:
    file = open(basedir + i, 'r')
    [sequence,acc_nm] = sequence_reader(file)
    comp_vector = calc_comp_vector(sequence)
    acc_nm_list.append(acc_nm)
    comp_vectors.append(comp_vector)

distance_matrix = generate_distance_matrix(acc_nm_list,comp_vectors)
Phylip_format_matrix(acc_nm_list, distance_matrix)
