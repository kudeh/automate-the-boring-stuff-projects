from Node import Node

class SinglyLinkedList:
    """
       
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """

        """
        newNode = Node(data)

        if self.head:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

        self.size += 1

    def delete(self, data):

        current = self.head
        prev = self.head

        while current.next:

            if current.data == data:
                if current == self.head:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                
                self.size -= 1
            
            prev = current
            current = current.next

    def search(self, data):

        for s in self.iterate():

            if data == s:
                return True

        return False


    def iterate(self):
        """

        """
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

if __name__ == '__main__':

    s = SinglyLinkedList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)

    s.delete(2)
    
    current = s.head
    for n in s.iterate():
        print(n)

    print(s.size)
    print(s.search(2))
    print(s.search(4))

            
