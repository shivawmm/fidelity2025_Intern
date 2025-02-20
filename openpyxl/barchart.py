from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
data = [["Year", "Sales"],
        [2020, 100],
        [2021, 120],
        [2022, 150],
        [2023, 180],
        [2024, 200]]

wb = Workbook()
sh = wb.active
for s in data:
    sh.append(s)
bar = BarChart()
data = Reference(sh, min_col=1, min_row=2, max_row=5, max_col=2)
categories = Reference(sh, min_col=1, min_row=2, max_row=5)
sh.add_chart(bar, "E2")
bar.set_categories(categories)
bar.add_data(data, "E7")
wb.save("chart.xlsx")