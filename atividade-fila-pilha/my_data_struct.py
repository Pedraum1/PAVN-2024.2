from typing import Any
from dataclasses import dataclass

@dataclass
class Node:

    data: Any
    next = None

class Queue:
    '''
    A simple class to model  a queue
    '''

    def __init__(self):
        self.first = self.last = None
        self.length = 0

    def push(self, data: Any) -> None:
        node = Node(data)

        if self.is_empty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.length += 1

    def pop(self) -> Any:
        if self.is_empty():
            return None
        
        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        self.length -= 1

        return data

    def __str__(self):
        if self.is_empty():
            return 'Queue is empty.'
            
        string = ''
        node = self.first
        while node:
            string += f'{node.data} -> '
            node = node.next

        return string

    def is_empty(self) -> bool:
        return self.length == 0
    
    def peek(self) -> Any:
        if self.is_empty():
            return None
        
        return self.first.data
    
    def __len__(self) -> int:
        return self.length


class Stack:
    '''
    A simple class to model  a queue
    '''

    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, data: Any) -> None:
        node = Node(data)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self) -> Any:
        if self.is_empty():
            return None
        
        node = self.top
        self.top = self.top.next
        self.length -= 1
        return node.data
    
    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self.top.data
    
    def __str__(self) -> str:
        if self.length == 0:
            return 'Empty stack.'
        
        string = ''
        node = self.top
        while node:
            string += f'{node.data}\n'
            node = node.next

        return string

    def __len__(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0