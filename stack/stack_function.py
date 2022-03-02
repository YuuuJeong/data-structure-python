from typing import Any

class Stack:


    class Empty(Exception):

        pass

    class Full(Exception):

        pass

    def __init__(self, capacity : int) -> None:

        self.stk = [None] * capacity
        self.capacity = capacity
        self.top = 0


    def __len__(self) -> int:
        return self.top

    def is_empty(self) -> bool:

        return self.top <= 0

    def is_full(self) -> bool:
        return self.top >= self.capacity

    def push(self, value = Any) -> None:

        if self.is_full():
            raise Stack.Full
        self.stk[self.top] = value
        self.top += 1

    def pop(self) -> Any:

        if self.is_empty():
            raise Stack.Empty
        self.top -= 1
        return self.stk[self.top - 1]

    def peek(self) -> Any:

        if self.is_empty():
            raise Stack.Empty
        return self.stk[self.top - 1]
    
    def clear(self) -> None:

        self.top = 0

    def find(self, value:Any) -> Any:

        for i in range(self.top -1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value:Any) -> int:

        data_num = 0
        for i in range(self.top):
            if self.stk[i] == value:
                data_num += 1
        return data_num

    def __contains__(self, value:Any) -> bool:
        return self.count(value)

    def dump(self) -> None:

        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.top])

    
