
# Element is a single unit in Linked List
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# in a Linked List, the head pointer point to the first element
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            # we are iterating the list to reach to its end (the lastest element)
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        i = 1
        if self.head:
            while i != position:
                current = current.next
                i += 1
            return current
        else:
            return None

    def insert(self, new_element, position):
        current = self.head
        i = 1
        while i != position-1:
            current = current.next
            i += 1
        temp = current.next
        current.next = new_element
        current.next.next = temp


    def delete(self, value):
        current = self.head
        if current:
            i = 1
            # Finding the position of the deletion candidate
            while current.value != value:
                current = current.next
                i += 1

            current = self.head
            j = 1
            while j != i:
                current = current.next
                j += 1
            if j == 1:
                # if the head element must be deleted,
                # so, we have to change the head to the second element
                self.head = self.head.next
            else:
                current.next = current.next.next



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# # Test insert
ll.insert(e4,3)
# # Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
