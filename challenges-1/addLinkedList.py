import sys
from linkedList import LinkedListNode

def add(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    head = None
    prev = None
    rem, carry = 0, 0
    while head1 != None or head2 != None:
        if head1 != None:
            a = head1.getValue()
        else:
            a = 0

        if head2 != None:
            b = head2.getValue()
        else:
            b = 0

        rem = a + b + carry
        if rem >= 10:
            carry = 1
            rem = rem % 10
        else:
            carry = 0
        node = LinkedListNode(rem)
        if head == None:
            head = node
            prev = head
        else:
            prev.setNext(node)
            prev = prev.getNext()

        if head1 != None:
            head1 = head1.getNext()
        if head2 != None:
            head2 = head2.getNext()

    if carry != 0:
        node = LinkedListNode(carry)
        prev.setNext(node)

    return head

def main():
    arr1 = [1,2,3]
    arr2 = [1,2]
    head1, head2 = None, None
    head1 = LinkedListNode(None)
    head2 = LinkedListNode(None)
    head1.setValuesFromArray(arr1)
    head2.setValuesFromArray(arr2)

    head = None
    head = add(head1, head2)
    head.display()
    print

    arr3 = [7,8,9]
    head3 = None
    head3 = LinkedListNode(None)
    head3.setValuesFromArray(arr3)

    res = None
    res = add(head1, head3)
    res.display()

if __name__ == "__main__":
    main()
