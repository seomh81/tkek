# CSV파일 읽기
import csv

f = open('file_name.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdf:
    print(line)
f.close()

# CSV파일 쓰기
import csv

f = open('output.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow([1, "Alice", True])
wr.writerow([2, "Bob", False])
f.close()

# Intermediate 있어보이게 표현
'''
with open('./train.csv') as csvfile:
    rdr = csv.DictReader(csvfile))
    for i in rdr:
      print(i)
'''

# Advanced pandas로 읽기
import numpy as pd

train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")

# train 데이터 살펴보기
train.describe(include="all")
