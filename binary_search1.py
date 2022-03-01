from typing import Sequence, Any
import copy

def bin_search(arr : Sequence, key:Any) -> int:
    first = 0
    last = len(arr)-1

    copy_arr = copy.deepcopy(arr)
    copy_arr.sort()
    while True:
        mid = (first + last) // 2
        if first > last :
            break

        if key > copy_arr[mid]:
            first = mid + 1
        elif key == copy_arr[mid]:
            return mid
        else:
            last = mid -1
    return -1
if __name__ == '__main__':
    num = int(input('데이터 숫자 입력해주세요.'))
    data = [None] * num

    for i in range(num):
        data[i] = int(input('데이터 숫자 배열에 넣어주세요.'))

    key = int(input('찾고자 하는 숫자는?'))

    index = bin_search(data, key)

    if index == -1:
        print("탐색 실패")
    else :
        print('{}번째 인덱스에 있네요.'.format(index+1))
