import pandas as pd

# 16번째 row를 헤더로 지정해서 엑셀 읽기
df_free_repair = pd.read_excel('CallReportAll_2006.xlsx', header=16)

# loc 이용해 필요한 열 추출
df_free_repair = df_free_repair.loc[:, ['보수호기코드', '일자', '고장부위', '매니저', '내용', '운행정지', '갇힘', '도착시 승객갇힘', '유상수리', 'NOF']]

# 고장접수내용 수정(괄호)삭제 내용 간단히
# 우측에서 ( 괄호 좌측 것 쓰기
df_free_repair['고장부위'] = df_free_repair['고장부위'].apply(lambda x: x.split('(')[1])
# 좌측에서 ) 괄호 우측 것 쓰기
df_free_repair['고장부위'] = df_free_repair['고장부위'].apply(lambda x: x.split(')')[-1])

# 짧은 내용은 스마트리포트에 표기 안됨. 강제로 6글자 스페이스바
df_free_repair['고장부위'] = df_free_repair['고장부위'].str.ljust(width=7, fillchar=' ')

# 오름차순 정렬
df_free_repair = df_free_repair.sort_values(by=['보수호기코드', '일자'], ascending=True)
# df_free_repair = df_free_repair.sort_values(by=['보수호기코드'], ascending=False)

# 중복제거 호기&내용
df_free_repair = df_free_repair.drop_duplicates(['보수호기코드', '고장부위'], keep=False)

# print(df_free_repair)
# print(df_item1)

df_free_repair.to_excel('free_repair.xlsx')
