from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int :
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(len(x)):
        x[i] = int(input('데이터들을 입력해주세요.'))

    ky = int(input("찾고자 하는 데이터 숫자값을 입력해주세요."))

    index  = seq_search(x, ky)

    if index == -1:
        print("탐색 실패!")
    else:
        print('찾고자 하는 데이터는 {}번째에 있습니다.'.format(index+1))

