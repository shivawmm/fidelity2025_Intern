from openpyxl import Workbook
wb = Workbook()
sh = wb.active
sh['A1'] = 10
sh['A2'] = 20
sh['A3'] = 30
sh['A4'] = 40
sh['A5'] = 50
wb.save("Book2.xlsx")