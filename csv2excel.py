import os
import pandas as pd

print("A KayVeez lab program. Convert any csv file to excel...\n")
b=input('Press Enter to start converting files...\n')


path1='csv_files'
path2='excel_files'
checker=0
if not os.path.exists(path1):
    os.makedirs(path1)

    checker=1

else:
    pass
if not os.path.exists(path2):
    os.makedirs(path2)
else:
    pass


if checker==0:
    files = os.listdir('csv_files')
    print('\nChecking if CSV files are present')
    i = 0
    for file in files:
        if file.endswith('.csv'):
            i+=1
        else:
            pass
    if i>0:
        print('\nConverting...')
        for file in files:
            if file.endswith('.csv'):
                try:
                    # reading the csv file
                    cvsDataframe = pd.read_csv(f'csv_files/{file}')

                    # creating an output excel file
                    resultExcelFile = pd.ExcelWriter(f'excel_files/{file.removesuffix(".csv")}.xlsx')

                    # converting the csv file to an excel file
                    cvsDataframe.to_excel(resultExcelFile, index=False)

                    # saving the excel file
                    resultExcelFile.save()
                except Exception as e:
                    print(f'\nSome error occurred. Please check this csv file --> {file}.\n')
                    continue
    else:
        print('\nNo CSV file found. Please copy the program in a folder with CSV files and try again.\n')
        pass
else:
    print('\n"csv_files" folder did not exist, run program after copying ".csv" files into the "csv_files" folder ...\n')
a=input('\nThanks for using my converter. Press Enter to exit....\n')
