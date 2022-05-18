def est_base(c):
    if c == 'A' or c == 'T' or c == 'G' or c == 'C':
        return True
    else:
        return False


def est_adn(s):
    i = 0
    s = str(s)
    while i < len(s):
        s1 = s[i]
        testadn = est_base(s1)
        if testadn == False:
            return False
        i += 1
    return True


def arn(adn):
    testadn = est_adn(adn)
    if testadn == False or len(adn) == 0:
        return None
    i = 0
    sequence_arn = ''
    while i < len(adn):
        s = adn[i]
        if s == 'T':
            sequence_arn += 'U'
        else:
            sequence_arn += adn[i]
        i += 1
    return sequence_arn



def arn_to_codons(arn):
    i = 0
    codon = []
    while i < len(arn):
        res = ""
        while len(res) < 3:
            res += arn[i]
            i += 1
        codon.append(res)
        if len(arn) - i < 3:
            return codon
    return codon


def load_dico_codons_aa(filename):
    from json import loads
    fichier = open(filename, "r")
    strjson=fichier.read()
    fichier.close()
    lejson = loads(strjson)
    return lejson


def codons_stop(dico):
    tab = ['AAA', 'AAU', 'AAG', 'AAC', 'AUA', 'AUU',
    'AUG', 'AUC', 'AGA', 'AGU', 'AGG', 'AGC',
    'ACA', 'ACU', 'ACG', 'ACC', 'UAA', 'UAU', 
    'UAG', 'UAC', 'UUA', 'UUU', 'UUG', 'UUC', 
    'UGA', 'UGU', 'UGG', 'UGC', 'UCA', 'UCU', 
    'UCG', 'UCC', 'GAA', 'GAU', 'GAG', 'GAC', 
    'GUA','GUU', 'GUG', 'GUC', 'GGA', 'GGU', 
    'GGG', 'GGC', 'GCA', 'GCU', 'GCG', 'GCC', 
    'CAA', 'CAU', 'CAG', 'CAC', 'CUA','CUU', 
    'CUG', 'CUC', 'CGA', 'CGU', 'CGG',
    'CGC', 'CCA', 'CCU', 'CCG','CCC']
    i = 0
    res = []
    while i < len(tab):
        if tab[i] not in dico:
            res.append(tab[i])
            i += 1
        else: 
            i += 1
    return res


def codons_to_aa(codons, dico):
    tab = codons_stop(dico)
    i = 0
    res = []
    while i < len(codons):
        if codons[i] in tab:
            return res
        else:
            res.append(dico[codons[i]])
        i += 1
    return res 



def nextIndice(tab, ind, elements):
    res = [] 
    while ind < len(tab):
        i = 0
        while i < len(elements):
            if tab[ind] == elements[i]:
                res.append(elements[i])
            i += 1
        ind += 1
    if len(res) == 0:
        return len(tab)
    return res


def decoupe_sequence(seq, start, stop):
    i = 0
    res1 = []
    while i < len(seq):
        if seq[i] in start:
            res = []
            i += 1
            while seq[i] not in stop:
                res.append(seq[i])
                i += 1
            res1.append(res)
        i += 1
    return res1

