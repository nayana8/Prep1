import sys

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def setValuesFromArray(self, arr):
        if len(arr) == 0:
            return

        if len(arr) == 1:
            self.value = arr[0]
            return

        for i,x in enumerate(arr):
            if i == 0:
                self.value = x
                prev = self
            else:
                node = LinkedListNode(x)
                prev.setNext(node)
                prev = prev.getNext()

    def display(self):
        if self.value == None:
            print ("Empty list")
        else:
            cur = self
            while cur != None:
                print cur.value,
                cur = cur.getNext()


def main():
    head = None
    arr = [1,2,3]
    head = LinkedListNode(None)
    head.setValuesFromArray(arr)

    assert arr[0] == head.getValue()
    assert None != head.getNext()
    assert arr[1] == head.getNext().getValue()
    assert None != head.getNext().getNext()
    assert arr[2] == head.getNext().getNext().getValue()
    assert None == head.getNext().getNext().getNext()

    head.display()

if __name__ == "__main__":
    main()
