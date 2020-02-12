class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def insert(self,new_element):
        new_element.next = self.head
        self.head = new_element
    def delete_first(self):
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None

# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
ll = Linkedlist()
ll.append(e1)
ll.append(e2)
ll.insert(e3)
ll.delete_first()
print()