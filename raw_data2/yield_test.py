my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


def divide_list(l, n):
    # 리스트 l의 길이가 n이면 계속 반복
    for i in range(0, len(l), n):
        yield l[i:i + n]


# 한 리스트에 몇개씩 담을지 결정
n = 7

result = list(divide_list(my_list, n))
print(result)
