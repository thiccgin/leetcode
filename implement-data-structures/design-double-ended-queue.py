class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        to_pop = self.tail.prev
        new_last = to_pop.prev
        new_last.next = self.tail
        self.tail.prev = new_last

        return to_pop.value


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        to_pop = self.head.next
        new_first = to_pop.next
        self.head.next = new_first
        new_first.prev = self.head

        return to_pop.value

