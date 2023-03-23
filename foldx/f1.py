import os
import time
import shutil

#This program is for Windows only!
 
#This uses foldx_4. If you wish to use foldx_5 delete foldx_4.exe and rotabase.txt, for all instances of foldx_4.exe in the program replace with foldx_5.exe 

def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]
kv = input('This is one of the programs from the lab of KayVeez.\nIt performs FoldX calculations for individual residues autonomously.\nPress Enter to continue......')
path1 = 'mutant'
if not os.path.exists(path1):
    os.makedirs(path1)
else:
    shutil.rmtree(path1)  # Removes all the subdirectories!
    os.makedirs(path1)
path2 = 'i_list'
if not os.path.exists(path2):
    os.makedirs(path2)
else:
    shutil.rmtree(path2)  # Removes all the subdirectories!
    os.makedirs(path2)


a = remove_newlines("individual_list.txt")
print(a)
i=1

for file in a:
    with open(f'i_list/individual_list_{i}.txt', 'w') as f:
        f.write(f'{file}')
        i+=1

for pos in range(len(a)):
    pois=str(pos)
    s = a[pos]
    s1 = s.replace(";", "")
    path = f'mutant/{s1}'
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)  # Removes all the subdirectories!
        os.makedirs(path)

    os.system(f'foldx_4.exe --command=BuildModel --pdb=1.pdb --mutant-file=i_list/individual_list_{pos+1}.txt --numberOfRuns=1 --temperature=298 --pH=7 --vdwDesign=2 --ionStrength=0.05 --output-dir=mutant/{s1} --output-file={s1}')

files =[]
for pos in range(len(a)):
    s = a[pos]
    s1 = s.replace(";", "")
    files.append(os.listdir(f'mutant/{s1}'))
    os.system(f'foldx_4.exe --command=Stability --pdb-dir=mutant/{s1} --pdb=1_1.pdb > mutant/{s1}/stability_info.txt')

for pos in range(len(a)):
    s = a[pos]
    s1 = s.replace(";", "")
    print(a[pos])
    with open('stability_output.txt','a') as final:
        with open(f"mutant/{s1}/stability_info.txt", "r") as searchfile:
            for line in searchfile:
                if "Total          =" in line:
                    stb = line
                    msg = f'Stability of {s1} is {stb[23:]}'
                    final.write(msg)
    with open('excel_readings.txt','a') as final1:
        with open(f"mutant/{s1}/stability_info.txt", "r") as searchfile1:
            for line1 in searchfile1:
                if "Total          =" in line1:
                    stb1 = line1
                    final1.write(stb1[23:])

del_dat = input('Do you want to keep run data? Yes/No : ')
del_d = del_dat.lower()
if del_d == 'no' or del_d=='n':
    shutil.rmtree('mutant')
    shutil.rmtree('i_list')
    filez = os.listdir()
    for file in filez:
        if file.endswith('fxout'):
            os.remove(f'{file}')
elif del_d == 'yes' or del_d =='y':
    pass
c=input('Thank you for using my program! Press Enter to exit! :)')



