import openpyxl
web_obj = openpyxl.load_workbook('Book1.xlsx')
sh_obj = web_obj.active
cell_obj = sh_obj.cell(row=1, column=1)
# print(cell_obj.value)
rows = sh_obj.max_row
cols = sh_obj.max_column

# print(rows, cols)
# for i in range(1, rows+1):
#     print(sh_obj.cell(row = i, column = 1 ).value)

headers = [sh_obj.cell(row=1, column=j).value for j in range(1, cols + 1)]
data_dict = {header: [] for header in headers}
for i in range(2, min(12, sh_obj.max_row + 1)): 
    for j in range(1, cols + 1):
        data_dict[headers[j - 1]].append(sh_obj.cell(row=i, column=j).value)

print(data_dict)

# for i in range(1, 12):
#     for j in range(1, cols+1):
#         print(sh_obj.cell(row = i, column = j).value, end=" ")
#     print()

