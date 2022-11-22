import math
def shannon_entropy(dna_sequence):
    """Custom implementation of shannon entropy with a full non-binarized sequence
        Formula looks like this
        H(S) = −Σ P(Si) log2 (P(Si))
        P(Si) is a bit confusing but, it's the relative frequency of the current char i in the whole string 
        as we are iterating on each character in the string. 
    """
    
    # Hold the relative frequency per nucleotide for a given dna sequence
    relative_freq_nucleotide = {
        'A' : 0, 
        'T' : 0, 
        'G' : 0, 
        'C': 0,
        'N' : 0
    }
    
    # Formula looks like this
    # H(S) = −Σ P(Si) log2 (P(Si))
    # P(Si) is a bit confusing but, it's the relative frequency of the current char i in the whole string 
    # as we are iterating on each character in the string. 

    
    # step 1: calculate all the frequency for each characters
    for nucleotide in relative_freq_nucleotide:
        relative_freq_nucleotide[nucleotide] = dna_sequence.count(nucleotide) / len(dna_sequence)
    
    # step 2: iterate over each nucleotide and sum up the relative frequency
    negative_entropy = 0
    for nucleotide_i in dna_sequence:
        rel_freq = relative_freq_nucleotide[nucleotide_i]
        negative_entropy = negative_entropy + (rel_freq * math.log(rel_freq, 2))
        
    return -negative_entropy