dna = 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'

def init_dna():
    hair_list = [('Black', 'CCAGCAATCGC'), ('Brown', 'GCCAGTGCCG'), ('Blonde', 'TTAGCTATCGC')]
    face_list = [('Square', 'GCCACGG'), ('Round', 'ACCACAA'), ('Oval', 'AGGCCTCA')]
    eye_list = [('Blue', 'TTGTGGTGGC'), ('Green', 'GGGAGGTGGC'), ('Brown', 'AAGTAGTGAC')]
    gender_list = [('Female', 'TGAAGGACCTTC'), ('Male', 'TGCAGGAACTTC')]
    race_list = [('White', 'AAAACCTCA'), ('Black', 'CGACTACAG'), ('Asian', 'CGCGGGCCG')]

    return [hair_list, face_list, eye_list, gender_list, race_list]
dna_suspect = []
def search_suspect(dna):
    dna_record = init_dna()
    for dna_part in dna_record:
        for prop in dna_part:
            if prop[1] in dna:
                dna_suspect.append(prop[0])


search_suspect(dna)
print(dna_suspect)