#!/usr/bin/env python
# coding: utf-8

# In[57]:


# The tasks done:
# Manually downloaded the DNA and protein data from https://www.ncbi.nlm.nih.gov/nuccore/NM_207618.2
# Imported the data into python 
# Created an algorithm to translate DNA data into protein
# Checked if translation matches our downloaded protein file


# In[58]:


# STEPS:

# check if the length of the is divisible by 3
    # loop over the sequence
        # extract a single codon
        # look up the codon and store the result


# In[59]:


def translate(seq):
    """translate."""
    table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
    protein = ""        
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]
    
    return protein


# In[60]:


def read_sequence(inputfile):
    """Reads and returns the input sequence with special charecters removed."""
    with open(inputfile, "r") as f: # "r" is the short form of read
        seq = f.read()    # This actually contains the contex of the file
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq


# In[61]:


prt = read_sequence("protein.txt")
DNA = read_sequence("DNA.txt")


# In[62]:


# translating the DNA file
# The location of the genes where the coding starts and ends: 21-938
#Instead of taking the entire DNA sequence, we would really like to be doing the translation 
#starting at position 21 and ending at 938.

translate(DNA[20:935])


# In[63]:


# Checking if the translation matches the protein
prt == translate(DNA[20:935])

