import math
from scipy import stats
import openpyxl

doc = 'benfordTests.xlsx'
wb = openpyxl.load_workbook(doc)
sheet = wb['sheetname']

#start at row 4, where the data starts in the Excel template
row = 4
for i in range(row, sheet.max_row):
    print(sheet['a'+str(row)].value)
    #set y variable, the numerical frequencies recorded in each Excel row
    y = []
    for cellObj in sheet['c'+str(row):'k'+str(row)]:
        for i in cellObj:
            y.append(i.value)
    #set x variable, Benford's distribution, which will be used to explain the observed numerical frequencies of the data
    x = []
    for i in range(1,10):
        x.append(math.log10((1+i)/i))

    #write stats for each row to their relative column in the Excel template
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    sheet['o'+str(row)].value = float(slope)
    sheet['p'+str(row)].value = float(intercept)
    sheet['q'+str(row)].value = float(r)
    sheet['r'+str(row)].value = float(p)
    sheet['s'+str(row)].value = float(std_err)
    wb.save('benfordTests_copy.xlsx')
    
    #move on to next row
    row +=1

#close Excel file to prevent bugs
wb.close()
