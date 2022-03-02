from stack_function import Stack
from enum import Enum

Menu = Enum('Menu', ['push', 'pop', 'peek', 'find','dump', 'exit'])

def select_menu():

    s = [f'({menu.value}){menu.name}' for menu in Menu]

    while True:
        print(*s, sep= '  ', end='')
        n = int(input(': '))
        if 1<= n <= len(Menu):
            return Menu(n)

s = Stack(64)


while True:
    print(f'현재 데이터 개수는: 최대 개수인 {s.capacity}개 중 {len(s)}개입니다.')

    menu = select_menu()

    if menu == Menu.push:
        x = int(input('스택에 넣을 데이터를 입력해주세요.: '))
        try:
            s.push(x)
        except Stack.Full:
            print('스택이 가득찼습니다.')
    elif menu == Menu.pop:
        try:
            x= s.pop()
            print('맨 위에서 꺼낸 데이터는 {}입니다.',format(x))
        except Stack.Empty:
            print('스택이 비어있습니다.')
    elif menu == Menu.peek:
        try:
            x= s.peek()
            print('맨 위에서 꺼낸 데이터는 {}입니다.'.format(x))
        except Stack.Empty:
            print('스택이 비어있습니다.')
    elif menu == Menu.find:
        x = int(input('찾아볼 값을 입력해주세요.:'))
        if x in s:
            print('{}개 포함되고, 맨 앞의 위치는 {}입니다'.format(s.count(x), s.find(x)))
        else:
            print('찾는 값이 없습니다.')
    elif menu == Menu.dump:
        s.dump()
    else:
        break
