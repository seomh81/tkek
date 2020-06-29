"""
Author : Byunghyun Ban
Last Modification : 2018.12.27.
"""

import os

directory = "raw_data/"
outfile_name = "list.csv"

out_file = open(outfile_name, 'w')

files = os.listdir(directory)

headers = []
outfile_has_header = True  # False라면, 헤더값을 입력해줌

for filename in files:  # 반복수행
    if ".his" not in filename:  # his파일만 수행하게(1)
        continue  # his파일만 수행하게(2)
    file = open(directory + filename)  # 파일생성 후 file이라는 이름의 변수로 초기화
    contents = []  # 텅빈 리스트를 새롭게 초기화, 파일을 부를때마다 초기화
    for line in file:  # 한줄씩 차례대로 위에서 끝까지 불러오고, 마지막 줄 후 종료
        if "=" in line:  # 내부에 =가 없으면 수행하지 않을 것
            splits = line.split("=")  # =를 기준으로 스트링을 쪼개줌, 한줄씩 데이터 쪼개줌, 2개 원소를 갖는 리스트 작성되어 splits에 저장됨, 0은 헤더, 1은 컨텐트
            contents.append(splits[-1].strip())  # 라인 우측값에서 좌우공백을 벗겨내는 strip 실행
            if len(contents) > len(headers):  # 헤더와 컨텐트 길이 비교. 핵심부분.
                headers.append(splits[0].strip())

    if not outfile_has_header:  # outfile에 헤더가 있는지 검사
        header = ", ".join(headers)  # join함수로 헤더 내용물 사이에 ,로 스트링 삽입
        out_file.write(header)
        outfile_has_header = True

    new_line = ", ".join(contents)  # join함수로 컨텐트 사이에 ,삽입
    out_file.write("\n" + new_line)  # join을 통해 완성된 new line을 out_file에 적어줌

    file.close()  # 파일 하나를 다 읽을 때마다 종료해줌
out_file.close()  # out_file 작성이 끝나서 파일 종료
