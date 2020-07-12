import pandas as pd

# 16번째 row를 헤더로 지정해서 엑셀 읽기
df_free_repair = pd.read_excel('CallReportAll_2006.xlsx', header=16)
# EL관리현황에서 보수코드 JOB NO로 가져오기
df_el_maintain = pd.read_excel('202006월EL관리현황(전국).xlsx')

# loc 이용해 필요한 열 추출
df_free_repair = df_free_repair.loc[:,
                 ['Job Number', '일자', '고장부위', '매니저', '내용', '운행정지', '갇힘', '도착시 승객갇힘', '유상수리', 'NOF']]
df_el_maintain = df_el_maintain.loc[:, ['JOB-NO', '보수코드']]

# Vlookup처럼 쓰기위해 헤더 이름 통일
df_free_repair.rename(columns={'Job Number': 'JOB-NO'}, inplace=True)

# Vlookup과 유사하게 사용
df_free_repair = pd.merge(df_free_repair, df_el_maintain, on='JOB-NO', how='left')

# 데이터 재 정렬
df_free_repair = df_free_repair.loc[:, ['보수코드', '일자', '고장부위', '매니저', '내용', '운행정지', '갇힘', '도착시 승객갇힘', '유상수리', 'NOF']]

# 고장접수내용 수정(괄호)삭제 내용 간단히
# 우측에서 ( 괄호 좌측 것 쓰기
df_free_repair['고장부위'] = df_free_repair['고장부위'].apply(lambda x: x.split('(')[1])
# 좌측에서 ) 괄호 우측 것 쓰기
df_free_repair['고장부위'] = df_free_repair['고장부위'].apply(lambda x: x.split(')')[-1])

# 매니저 이름만 쓰기
df_free_repair['매니저'] = df_free_repair['매니저'].str.split('(').str[0]

# 짧은 내용은 스마트리포트에 표기 안됨. 강제로 6글자 스페이스바
df_free_repair['고장부위'] = df_free_repair['고장부위'].str.ljust(width=7, fillchar=' ')

# 긴 글자 자르기
df_free_repair['고장부위'] = df_free_repair['고장부위'].str[:10]
df_free_repair['내용'] = df_free_repair['내용'].str[:13]

# 오름차순 정렬
df_free_repair = df_free_repair.sort_values(by=['보수코드', '일자'], ascending=True)
# df_free_repair = df_free_repair.sort_values(by=['보수호기코드'], ascending=False)

# 중복제거 호기&내용
df_free_repair = df_free_repair.drop_duplicates(['보수코드', '고장부위'], keep='first')

# 고장부위 빈 열 제거
df_free_repair = df_free_repair.drop(df_free_repair[df_free_repair['고장부위'] == '       '].index)

# 중복 1,2,3 뽑아내기
df_free_dup1 = df_free_repair.drop_duplicates(['보수코드'], keep='first')
df_free_dup2 = df_free_repair.drop(df_free_repair[df_free_repair['index']] == df_free_dup1['index'])
df_free_dup2 = df_free_dup1.drop_duplicates(['보수코드'], keep='first')
df_free_dup3 = df_free_dup2.drop(df_free_dup2[df_free_dup2['index']] == df_free_dup1['index'])
df_free_dup3 = df_free_dup1.drop_duplicates(['보수코드'], keep='first')

# df_free_repair.reset_index(drop=True)

# df_free_dup = df_free_repair['보수코드'].value_counts()


# df_free_repair['count'] = df_free_repair['보수코드'].apply(df_free_repair['index'+1])

# 중복 갯수 세기
'''
for v in df_free_repair['보수코드']:
    if v not in df_free_repair['count']:
        i = 1
        df_free_repair['count'].append(i)
    else:
        i += 1
        df_free_repair['count'].append(i)
'''

# print(df_free_repair)
# print(df_item1)

df_free_repair.to_excel('free_repair.xlsx')
df_free_dup.to_excel('dup.xlsx')
