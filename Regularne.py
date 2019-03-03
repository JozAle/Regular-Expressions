import re

Tekst = ('CGGGGCTATGCAACTGGGTCGTCACATTCCCCTTTCGATA',
         'TTTGAGGACGTACGTACGATGCAACTCCAAAGCGGACAAA',
         'GGATGCAACTGATGCCGTTTGACGACCTAAATCAACGGCC',
         'AAGGATGCAACTCGACGTACGTACGAGCTGGTTCTACCTG',
         'AATTGGTCTAAAAAGATTATAATGTCGGTCCATGCAACTT',
         'CTGCTGTACAACTGAGATCATGCTGCATGCAACTTTCAAC',
         'TACATGATCTTTTGATGCAACTTGGATGAGGGAATGATGC',
         'ATGACGTACGTACGACTGACGTACCGACGCATGCAACTTC',)

with open('Wynik.txt','w') as plik:
    print('Wyniki wyszukiwania: ',file=plik)

with open('Wynik.txt','a') as plik:
    for Sekwencja in Tekst:
        print(Sekwencja,file=plik)
        for Znalezione in re.finditer('(GC)+', Sekwencja):
            print('Jest',Znalezione.group(),'na pozycji od indeksu',Znalezione.start(),'do',Znalezione.end(),file=plik)    
    print('',file=plik)
    
    for Sekwencja in Tekst:
        print(Sekwencja,file=plik)
        for Znalezione in re.finditer('(G.C|C.G)', Sekwencja):
            print('Jest',Znalezione.group(),'na pozycji od indeksu',Znalezione.start(),'do',Znalezione.end(),file=plik)
    print('',file=plik)
    
    for Sekwencja in Tekst:
        print(Sekwencja,file=plik)
        for Znalezione in re.finditer('(GC[ATCG]{0,6}CG)', Sekwencja):
            print('Jest',Znalezione.group(),'na pozycji od indeksu',Znalezione.start(),'do',Znalezione.end(),file=plik)
    print('',file=plik)
    
    for Sekwencja in Tekst:
        print(Sekwencja,file=plik)
        for Znalezione in re.finditer('(CA+C)', Sekwencja):
            print('Jest',Znalezione.group(),'na pozycji od indeksu',Znalezione.start(),'do',Znalezione.end(),file=plik)
    print('',file=plik)

