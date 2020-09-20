import numpy as np
import xlrd
loc = "C:/Users/Asus/PycharmProjects/Stats-II_Project-1/dt.xlsx"
x = np.zeros(0)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(sheet.nrows):
  x= np.append(x,float(sheet.cell_value(i, 0)))
print(x)

for i in range(sheet.nrows):
