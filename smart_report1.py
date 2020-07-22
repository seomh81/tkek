import pandas as pd

# 16번째 row를 헤더로 지정해서 엑셀 읽기
df_breakdown_log = pd.read_excel('CallReportAll_2006.xlsx', header=16)
# EL관리현황에서 보수코드 JOB NO로 가져오기
df_el_maintailAll = pd.read_excel('202006월EL관리현황(전국).xlsx')

# loc 이용해 필요한 열 추출
df_breakdown_log = df_breakdown_log.loc[:,
                   ['Job Number', '일자', '고장부위', '매니저', '조치내용', '운행정지', '갇힘', '도착시 승객갇힘', '유상수리', 'NOF']]
df_el_maintailAll = df_el_maintailAll.loc[:, ['JOB-NO', '보수코드']]

# Vlookup처럼 쓰기위해 헤더 이름 통일
df_breakdown_log.rename(columns={'Job Number': 'JOB-NO'}, inplace=True)
df_breakdown_log.rename(columns={'조치내용': '내용'}, inplace=True)

# Vlookup과 유사하게 사용
df_breakdown_log = pd.merge(df_breakdown_log, df_el_maintailAll, on='JOB-NO', how='left')

# 데이터 재 정렬
df_breakdown_log = df_breakdown_log.loc[:, ['보수코드', '일자', '고장부위', '매니저', '내용', '운행정지', '갇힘', '도착시 승객갇힘', '유상수리', 'NOF']]

# 고장접수내용 수정(괄호)삭제 내용 간단히
# lambda 빼기
''''
# 우측에서 ( 괄호 좌측 것 쓰기
df_breakdown_log['고장부위'] = df_breakdown_log['고장부위'].apply(lambda x: x.split('(')[1])
# 좌측에서 ) 괄호 우측 것 쓰기
df_breakdown_log['고장부위'] = df_breakdown_log['고장부위'].apply(lambda x: x.split(')')[-1])
'''
# 우측에서 ( 괄호 좌측 것 쓰기
df_breakdown_log['고장부위'] = df_breakdown_log['고장부위'].str[5:]
# 좌측에서 ) 괄호 우측 것 쓰기
df_breakdown_log['고장부위'] = df_breakdown_log['고장부위'].str.split('(').str[0]

# 다른 표현 lambda 중복이 안됨.. 왜일까...
# 우측에서 ( 괄호 좌측 것 쓰기
df_breakdown_log['내용'] = df_breakdown_log['내용'].str[5:]
# 좌측에서 ) 괄호 우측 것 쓰기
df_breakdown_log['내용'] = df_breakdown_log['내용'].str.split('(').str[0]

# 매니저 이름만 쓰기, 이름 3자 표현
df_breakdown_log['매니저'] = df_breakdown_log['매니저'].str.split('(').str[0]
df_breakdown_log['매니저'] = df_breakdown_log['매니저'].str[:3]

# 짧은 내용은 스마트리포트에 표기 안됨. 강제로 6글자 스페이스바
df_breakdown_log['고장부위'] = df_breakdown_log['고장부위'].str.ljust(width=7, fillchar=' ')

# 긴 글자 자르기
df_breakdown_log['고장부위'] = df_breakdown_log['고장부위'].str[:10]
df_breakdown_log['내용'] = df_breakdown_log['내용'].str[:20]

# 고객과의 의견차 & 처리불가 / 접근 불가능, 고객통보 삭제
df_breakdown_log['내용'] = df_breakdown_log['내용'].replace(['접수 취소 / 고객과의 의견차'], '접수 취소')
df_breakdown_log['내용'] = df_breakdown_log['내용'].replace(['처리불가 / 접근 불가능, 고객통보'], '처리불가 / 접근 불가능')

# 오름차순 정렬
df_breakdown_log = df_breakdown_log.sort_values(by=['보수코드', '일자'], ascending=True)
# df_breakdown_log = df_breakdown_log.sort_values(by=['보수호기코드'], ascending=False)

# 중복제거 호기&내용
df_breakdown_log = df_breakdown_log.drop_duplicates(['보수코드', '고장부위'], keep='first')

# 고장부위 빈 열 제거
df_breakdown_log = df_breakdown_log.drop(df_breakdown_log[df_breakdown_log['고장부위'] == '       '].index)

# 중복 1,3,5 뽑아내기
df_breakdown_dup1 = df_breakdown_log.drop_duplicates(['보수코드'], keep='first')
df_breakdown_dup2 = df_breakdown_log.drop(df_breakdown_dup1.index)
df_breakdown_dup3 = df_breakdown_dup2.drop_duplicates(['보수코드'], keep='first')
df_breakdown_dup4 = df_breakdown_dup2.drop(df_breakdown_dup3.index)
df_breakdown_dup5 = df_breakdown_dup4.drop_duplicates(['보수코드'], keep='first')

# merge 로 합치기
# 합치기 전에 이름 변경
df_breakdown_dup3.rename(columns={'일자': '(2) 일자'}, inplace=True)
df_breakdown_dup3.rename(columns={'고장부위': '(2) 고장부위'}, inplace=True)
df_breakdown_dup3.rename(columns={'매니저': '(2) 매니저'}, inplace=True)
df_breakdown_dup3.rename(columns={'내용': '(2) 내용'}, inplace=True)
df_breakdown_dup3.rename(columns={'운행정지': '(2) 운행정지'}, inplace=True)
df_breakdown_dup3.rename(columns={'갇힘': '(2) 갇힘'}, inplace=True)
df_breakdown_dup3.rename(columns={'도착시 승객갇힘': '(2) 도착시 승객갇힘'}, inplace=True)
df_breakdown_dup3.rename(columns={'유상수리': '(2) 유상수리'}, inplace=True)
df_breakdown_dup3.rename(columns={'NOF': '(2) NOF'}, inplace=True)

df_breakdown_dup5.rename(columns={'일자': '(3) 일자'}, inplace=True)
df_breakdown_dup5.rename(columns={'고장부위': '(3) 고장부위'}, inplace=True)
df_breakdown_dup5.rename(columns={'매니저': '(3) 매니저'}, inplace=True)
df_breakdown_dup5.rename(columns={'내용': '(3) 내용'}, inplace=True)
df_breakdown_dup5.rename(columns={'운행정지': '(3) 운행정지'}, inplace=True)
df_breakdown_dup5.rename(columns={'갇힘': '(3) 갇힘'}, inplace=True)
df_breakdown_dup5.rename(columns={'도착시 승객갇힘': '(3) 도착시 승객갇힘'}, inplace=True)
df_breakdown_dup5.rename(columns={'유상수리': '(3) 유상수리'}, inplace=True)
df_breakdown_dup5.rename(columns={'NOF': '(3) NOF'}, inplace=True)

df_breakdown_merge = pd.merge(df_breakdown_dup1, df_breakdown_dup3, on='보수코드', how='left')
df_breakdown_merge = pd.merge(df_breakdown_merge, df_breakdown_dup5, on='보수코드', how='left')

'''
df_breakdown_log.to_excel('free_repair.xlsx')
df_breakdown_dup1.to_excel('dup1.xlsx')
df_breakdown_dup2.to_excel('dup2.xlsx')
df_breakdown_dup3.to_excel('dup3.xlsx')
df_breakdown_dup4.to_excel('dup4.xlsx')
df_breakdown_dup5.to_excel('dup5.xlsx')
'''
# 인덱스를 빼고 출력
df_breakdown_merge.to_excel('고장이력.xlsx', index=False)

del [[df_el_maintailAll, df_breakdown_log, df_breakdown_merge, df_breakdown_dup1, df_breakdown_dup2, df_free_dup3,
      df_breakdown_dup4, df_breakdown_dup5]]

###############무상이력 수식적용#################
# xls를 엑셀 프로그램을 이용해 xlsx로 바꿔야 함 else 에러뜸


df_free_parts = pd.read_excel('무상자재_2006.xlsx')
df_free_parts = df_free_parts.loc[:, ['repr_code', 'part_name']]

df_free_parts.to_excel('무상자재.xlsx', index=False)
