def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    length = len(dna)
    print(length)
    return length

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        print("True")
        return True
    else:
        print("False")
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    n = dna.count(nucleotide)
    print(n)
    return n

# count_nucleotides("ATCTAC", "G")


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if dna2 in dna1:
        print("True")
        return True
    else:
        print("False")
        return False

# contains_sequence("ATCGGC", "GGA")
    


def is_valid(dna):
    for i in dna:
        if i=="A" or i=="T" or i=="G" or i=="C":
            continue
        else:
            print("False")
            return False
    print(True)
    return True

# is_valid("ATCAB")

def insert_sequence(dna1, dna2, index):
    slice1 = dna1[0:index]
    slice2 = dna1[index:]
    seq = slice1 + dna2 + slice2
    print(seq)
    return seq

# insert_sequence("ATCC", "HV", 2)


def get_complement(nucleotide):
    dictionary = {
            'A':'T',
            'T':'A',
            'G':'C',
            'C':'G'
        }    
    # print(dictionary[nucleotide])
    return dictionary[nucleotide]

# get_complement('A')

def get_complementary_seq(dna):
    complement = ""
    for i in dna:
        complement = complement +  get_complement(i) + ""
    
    print(complement)

get_complementary_seq("ATGC")
