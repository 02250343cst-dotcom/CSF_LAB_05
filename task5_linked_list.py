class Node:
    def __init__(self, data):
        self.data, self.next = data, None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        self.head = Node(data) if not self.head else Node(data)
        self.head.next = self.head.next if self.head.next else None

    def insert_end(self, data):
        if not self.head:
            self.head = Node(data); return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next; return
        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next; return
            temp = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key: return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Test
ll = LinkedList()
ll.insert_end(10); ll.insert_end(20); ll.insert_end(30)
print("Original:", end=" "); ll.display()

ll.insert_begin(5)
print("After insert 5:", end=" "); ll.display()

ll.delete(20)
print("After delete 20:", end=" "); ll.display()

print(f"Search 30: {'Found' if ll.search(30) else 'Not found'}")