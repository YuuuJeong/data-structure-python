from typing import Any

class Queue:

    class Empty(Exception):

        pass

    class Full(Exception):

        pass


    def __init__(self, capacity : int):

        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.num = 0
        self.queue = [None] * capacity

    def __len__(self):

        return self.num

    def is_empty(self):

        return self.front == self.rear 

    def is_full(self):

        return self.num >= self.capacity

    def enque(self, x: Any)-> None:

        if self.is_full():
            raise Queue.Full

        self.queue[self.rear] = x
        self.num += 1
        self.rear = (self.rear + 1) % self.capacity

    def deque(self) :

        if self.is_empty():
            raise Queue.Empty
        value = self.queue[self.front]
        self.num -= 1
        self.front = (self.front +1 ) % self.capacity

        return value

    def peek(self) :

        if self.is_empty():
            raise Queue.Empty
        return self.queue[self.front]

    def find(self, value:Any) -> Any:

        for i in range(self.num):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                return idx
        return -1

    def count(self, value:Any) :

        value_num = 0
        for i in range(self.num):
            idx = (i +self.front) % self.capacity
            if self.queue[idx] == value:
                value_num += 1
        return value_num
    def __contains__(self, value:Any):

        return self.count(value)

    def clear(self):

        self.num = self.front = self.rear = 0

    def dump(self):
        if self.is_empty():
            print("큐가 비어있습니다.")
        else:
            for i in range(self.num):
                idx = (self.front + i) % self.capacity
                print(f"{self.queue[idx]}입니다", end ="")
            print()

    
