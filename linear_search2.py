from typing import Sequence, Any
import copy

def seq_search(arr:Sequence, key: Any)-> int:
    a = copy.deepcopy(arr)
    a.append(key) # 찾고자 하는 키를 마지막에 추가하여 종료조건을 줄이고자 함

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(arr) else i

if __name__ == '__main__':
    num = int(input('데이터를 몇 개 받을지 입력해주세요'))
    data = [None] * num

    for i in range(num):
        data[i] = int(input('data 입력해주세요'))

    key = int(input('찾고자 하는 숫자가 뭔가요?'))

    index = seq_search(data, key)

    if index == -1:
        print('탐색 실패!')
    else :
        print('찾고자 하는 데이터는 {}번째에 있네요.'.format(index+1))
