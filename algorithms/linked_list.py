class Node:
    previous = None
    next = None
    value = None

    def __init__(self, value):
        self.value = value

    def add(self, value):
        n = None

        if self.next is None:
            n = Node(value)
            self.next = n
            n.previous = self
        else:
            n = self.next.add(value)

        return n

    def remove(self):
        previous = self.previous
        next = self.next

        previous.next = next
        next.previous = previous

    def peerSort(self, peer):
        if self.value > peer.value:
            aux = self.value
            self.value = peer.value
            peer.value = aux
        else:
            peer.peerSort(self.next)
           

class LinkedList:
    head = None
    tail = None

    def add(self, value):
        n = None

        if self.head is None:
            n = Node(value)
            self.head = n
        else:
            n = self.head.add(value)

        if n.next is None:
            self.tail = n

        return n

    def remove(self, value):
        if self.head is not None and self.head.value == value:
            self.head.remove()

        elif self.tail is not None and self.tail.value == value:
            self.tail.remove()

        else:
            n = self.head

            while n != self.tail:
                
                if n.value == value:
                    n.remove()

                n = n.next

    
            

    def search(self, value):
        if self.head is not None and self.head.value == value:
            return self.head

        elif self.tail is not None and self.tail.value == value:
            return self.tail

        else:
            n = self.head

            while n != self.tail:
                
                if n.value == value:
                    return n

                n = n.next

    def traverse(self):
        if self.head is not None:
            l = []
            n = self.head

            while n is not None:
                l.append(n.value)

                n = n.next

            return l

    def sort(self):
        if self.head is not None:
            self.head.peerSort(self.head.next)
                    


            