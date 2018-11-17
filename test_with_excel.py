from xlrd import open_workbook
book = open_workbook('C:/Users/User/Downloads/KBiSP-2-kurs-1-sem.xlsx')
sheet = book.sheet_by_index(0)
for rowidx in range(sheet.nrows):
	row = sheet.row(rowidx)
	for colidx, cell in enumerate(row):
		if "БАСО-02-17 10.05.03(КБ-1)" == cell.value:
			print(colidx)
			print(rowidx)
			row_group = rowidx
			col_group = colidx
			row_monday = row_group+2
			row_vt = row_group+14
			row_sr = row_group+26
			row_cht = row_group+38
			row_pt = row_group+50
			row_cb = row_group+62

for i in range(0, 10):
	print(sheet.cell(row_monday, col_group).value)
	row_monday+=1

for i in range(0, 10):
	print(sheet.cell(row_vt, col_group).value)
	row_vt+=1

for i in range(0, 10):
	print(sheet.cell(row_sr, col_group).value)
	row_sr+=1

for i in range(0, 10):
	print(sheet.cell(row_cht, col_group).value)
	row_cht+=1

for i in range(0, 10):
	print(sheet.cell(row_pt, col_group).value)
	row_pt+=1
# rowidx - индексы столбцов
# colidx - индексы строк 
# cell.value - соделжимое столбца
6f04094bb3fc8a9e4b5d12ed61759a1f233556fdeaff68752d9c49dbd5dfe2e366f0c6f763f96da01a04f