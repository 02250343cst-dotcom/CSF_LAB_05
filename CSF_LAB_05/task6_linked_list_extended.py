class Node:
    def __init__(self, data):
        self.data, self.next = data, None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data); return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def count(self):
        c, temp = 0, self.head
        while temp:
            c += 1
            temp = temp.next
        return c
    def middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow.data if slow else None

    def reverse(self):
        prev, temp = None, self.head
        while temp:
            temp.next, prev, temp = prev, temp, temp.next
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Test
ll = LinkedList()
for i in [10, 20, 30, 40]:
    ll.append(i)
print("Original:", end=" "); ll.display()
print("Count:", ll.count())
print("Middle:", ll.middle())
ll.reverse()
print("Reversed:", end=" "); ll.display()