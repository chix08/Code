class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
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

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


# Temp
def append_temp(self, new_e):
    cur = self.next
    if cur:
        while cur.next:
            cur = cur.next
        cur.next = new_e
    else:
        self.next = new_e
        print()


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
print(ll.get_position(3).value)
ll.insert(e4, 3)
ll.delete(1)
# ll.get_position(3)

# E1 = Element(1)
# l1 = LinkedList()
# # append(l1,E1)
# E2 = Element(2)
# # append(l1,E2)
# E3 = Element(3)
# # append(l1,E3)
#
#
# append_temp(E1,E2)
# append_temp(E2,E3)
# print()
