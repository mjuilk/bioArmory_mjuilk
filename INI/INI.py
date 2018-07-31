#Rosalind | Introduction to the Bioinformatics Armory

with open('rosalind_ini.txt', 'r') as f:
    file = f.read()
    print (file.count('A'), file.count('C'), file.count('G'), file.count('T'))