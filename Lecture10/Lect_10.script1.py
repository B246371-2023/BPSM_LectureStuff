#!/usr/bin/python3

# Program to take a DNA sequence and calculate A+T content
# Written by s123456 on 20 Oct 2023
#--------------------------------------------#
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("A+T content is " + str(at_content))
