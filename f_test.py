import xlrd

df_free_parts = xlrd.open_workbook('무상자재_2006.xls')

# df_free_parts = pd.read_excel('무상자재_2006.xls')

# df_free_parts = df_free_parts.loc[:, ['repr_code', 'part_name']]


df_free_parts.to_excel('무상자재.xlsx', index=False)
