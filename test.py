# 라이브러리 불러오기
import numpy as np
import pandas as pd
import os

# 엑셀파일 내용 불러오기
# 디렉토리 세팅 (C:\\로 시작, 숫자앞에 \\, 나머진 \든 \\든 무관)
base_dir = os.getcwd()
excel_file = 'master.xlsx'
excel_dir = os.path.join(base_dir, excel_file)

# 엑셀읽기 as DataFrame to df_from_excel
df_from_excel = pd.read_excel(excel_dir,
    sheet_name = '운영 리스트', #해당 시트
    header = 3, #해당 row-1 값 (0부터 시작해서)
    #dtype = {'지사':str,
    #         '원장번호(원본)' : np.int64, #정수로
    #         '지점':str},
    index_col = 'No.',
    na_values = 'NaN',
    thousand = ',',
    #nrows = 10,
    comment = '#')

#데이터 확인
'''
print(df_from_excel)
print(df_from_excel.index)
print(df_from_excel.dtypes)
print(df_from_excel['지점'])
'''

# 데이터프레임을 엑셀 파일로 내보내기
# 저장할 엑셀이 열려있으면 에러 뜸
file_nm = "export4.xlsx" #내보낼 파일 이름 지정
xl_dir = os.path.join(base_dir, file_nm)

df_from_excel.to_excel(xl_dir, #해당 경로&이름으로 형식지정할거야
                       sheet_name = '신규', #시트이름 생성
                       na_rep='NaN', #null값 레퍼런스
                       float_format = "%.2f", #float 형식 지정, 소수점 2자리 반올림
                       header=True, #???
                       index=True, #???
                       index_label="No.",
                       startcol=1, #행을 시작순서, 1은 한 칸 뒤부터
                       startrow=1, #열, 상동
                       freeze_panes=(2,0) #???
                       )