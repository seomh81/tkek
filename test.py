# 라이브러리 불러오기
import numpy as np
import pandas as pd
import os

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("마스터파일 변환 프로그램")
root.geometry("400x80")
root.resizable(0,0)

def your_name() :
    yn = txt.get() #텍스트 입력란에서 값을 가져와 변수 yn에 저장
    lbl2.configure(text="your name:"+yn) #함수 실행 시 라벨2를 yn값으로 설정
    messagebox.showinfo("name",yn) #메세지 박스 띄움

lbl = Label(root, text = "경로를 입력해 주세요", font = "NanumGothic 10")
lbl.grid(row=0, column=0)
#lbl.pack()

txt = Entry(root)
txt.grid(row=0, column=1)
#txt.pack()

btn = Button(root, text = "OK", command=your_name, width = 3, height = 1)
btn.grid(row=1, column=1)
#btn.pack()

lbl2 = Label(root,text="your name : ")
lbl2.grid(row=2, column=1)


root.mainloop()




#엑셀 셀 내에 #이 있으면 그 이후는 모두 데이터 날아감 - 각주처리됨... 아놔

# 엑셀파일 내용 불러오기
# 디렉토리 세팅 (C:\\로 시작, 숫자앞에 \\, 나머진 \든 \\든 무관)
base_dir = os.getcwd()
excel_file = 'master.xlsx'
excel_dir = os.path.join(base_dir, excel_file)

# 엑셀읽기 as DataFrame to df_from_excel
df_from_excel = pd.read_excel(excel_dir,
    sheet_name = '운영 리스트', #해당 시트
    header = 3, #해당 row-1 값 (0부터 시작해서)
    dtype = {'호기':object
             },
    #dtype = {'지사':str,
    #         '원장번호(원본)' : np.int64, #정수로
    #         '지점':str},
    #index_col = 'No.',
    #na_values = 'NaN',
    #thousand = ',',
    #nrows = 10,
    comment = '#')

#데이터 확인 출력해서 보고싶다면...
'''
print(df_from_excel)
print(df_from_excel.index)
print(df_from_excel.dtypes)
print(df_from_excel['지점'])
'''

# 브이룩업을 위해선 데이터 시트가 하나 더 필요함
df_lookup = pd.read_excel(excel_dir,
                          sheet_name='운영 리스트',  # 해당 시트
                          header=3  # 해당 row-1 값 (0부터 시작해서)
                          )

# 수식비교해서 0번 칸에 넣음
df_from_excel.insert(0, '지사1', df_from_excel['호기코드11(원본)'].map(df_lookup.set_index('호기코드11(원본)')['지사']))

# 데이터프레임을 엑셀 파일로 내보내기
# 저장할 엑셀이 열려있으면 에러 뜸
file_nm = "export_브이룩업.xlsx" #내보낼 파일 이름 지정
xl_dir = os.path.join(base_dir, file_nm)

df_from_excel.to_excel(xl_dir, #해당 경로&이름으로 형식지정할거야
                       sheet_name = '신규', #시트이름 생성
                       #na_rep='NaN', #null값 레퍼런스
                       #float_format = "%.2f", #float 형식 지정, 소수점 2자리 반올림
                       header=True, #???
                       index=True, #???
                       index_label="No.",
                       startcol=0, #행을 시작순서, 1은 한 칸 뒤부터
                       startrow=0, #열, 상동
                       #freeze_panes=(2,0) #???
                       )