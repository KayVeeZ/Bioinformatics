import os
import pandas as pd

print("A KayVeez lab program. Convert any csv file to excel...")
b=input('Press Enter to start converting files...')
files = os.listdir()
print('Checking if CSV files are present')
i = 0
for file in files:
    if file.endswith('.csv'):
        i+=1
    else:
        pass
if i>0:
    print('Converting...')
    for file in files:
        if file.endswith('.csv'):
            try:
                # reading the csv file
                cvsDataframe = pd.read_csv(file)

                # creating an output excel file
                resultExcelFile = pd.ExcelWriter(f'{file.removesuffix(".csv")}.xlsx')

                # converting the csv file to an excel file
                cvsDataframe.to_excel(resultExcelFile, index=False)

                # saving the excel file
                resultExcelFile.save()
            except Exception as e:
                print(f'Some error occurred. Please check this csv file {file}.')
                continue
else:
    print('No CSV file found. Please copy the program in a folder with CSV files and try again.')
    pass

a=input('Thanks for using my converter. Press Enter to exit....')