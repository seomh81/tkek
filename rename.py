import os
from os import path


def main():  # 메인함수 선언
    for filename in os.listdir('.'):  # 현재 디렉토리에서 파일명 일괄 불러오기

        if filename[-3:] == 'BIN':  # 파일 확장자가 bin이면

            print('src =', filename)  # 파일 이름을 출력
            src = filename  # 파일 이름은 src에 넣기
            month = int(filename[-15:-13]) - 1  # 파일생성일 중 월을 추출해서 -1값을 month에 저장

            if month == 0:  # month가 0 이면 실행 (과거 일부 있었던 파일인 듯)
                # month = "{:0>2d}".format(month)
                month = '12'  # month를 12로 저장
                dst = filename[1:3] + '-' + filename[3:9] + '_' + str(int(filename[-17:-15]) - 1) + month + '.000'
                # 파일 중 L을 뺀 앞 2자리  -  6자리  _  년  월  .000 값으로 dst 값 저장 (과거 일부 있었던 파일인 듯)

                if path.exists(dst):  # dst값 같은 값이 존재한다면
                    print('duplicated, go to next...')  # 중복이니 다음으로 출력
                else:  # 중복이 아니면
                    os.rename(src, dst)  # 본래 파일명 src를 dst로 이름 변경
                    print('dst = ', dst)  # 변경이름 출력

            else:  # month가 0이 아닌 경우
                month = "{:0>2d}".format(month)  # 월 포맷을 00으로 선행 0을 표기
                dst = filename[1:3] + '-' + filename[3:9] + '_' + filename[-17:-15] + month + '.000'
                # 파일 중 L을 뺀 앞 2자리 - 6자리 _ 년월 .000 값으로 dst 값 저장
                print(dst)  # dst 값을 출력
                if path.exists(dst):  # dst값 같은 값이 존재한다면
                    print('duplicated, go to next...')  # 중복이니 다음으로 출력
                else:  # 중복이 아니면
                    os.rename(src, dst)  # 본래 파일명 src를 dst로 이름 변경
                    print('dst = ', dst)  # 변경이름 출력
    print('All files are successfully renamed...')  # for문이 끝나면 출력


# 메인함수 불러오기
if __name__ == '__main__':  # 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용
    main()
