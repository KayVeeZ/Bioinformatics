import os

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

kv = input('This is one of the programs from the lab of KayVeez.\nIt performs Maestro calculations for individual residues autonomously.\nPress Enter to continue......')
print('Program has started...please be patient, for long lists, it takes some time to run.')
a = remove_newlines("put.txt")

for file in a:
    os.system(f'maestro.exe config.xml 1.pdb --evalmut={file} >> mut.txt')

inputFile = "mut.txt"
outputFile = 'mutation_output.txt'

i = 0

with open(inputFile) as oldfile, open(outputFile, 'a') as newfile:
     for line in oldfile:
        if i==0:
            newfile.write(line)
            i+=1
        elif 'wildtype' not in line and '#structure' not in line:
            newfile.write(line)

os.remove('mut.txt')

kv1 = input("Thank you for using my program. Press Enter to continue....")