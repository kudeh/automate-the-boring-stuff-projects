class Node:
    """
    
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)

    node1.next = node2

    current = node1
    while(current):
        print(current.data)
        current = current.next


