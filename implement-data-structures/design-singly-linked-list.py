class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1 # Index out of bounds

    def insertHead(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next == None:
            self.tail = new_node

    def insertTail(self, value: int) -> None:
        self.tail.next = ListNode(value)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False    
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        found = []
        while curr:
            found.append(curr.value)
            curr = curr.next
        return found