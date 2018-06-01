import sys

class node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert(head, val):
    if head == None:
        head = node(val)
        return head
    temp = node(val)
    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = temp
    return head

def removeDuplicates(head):
    if head == None or head.next == None:
        return head

    cur = head
    temp = cur.next
    if cur.val == temp.val:
        while cur.val == temp.val:
            cur = cur.next
            temp = temp.next
    newHead = cur

    prev = None
    while cur != None:
        prev = cur
        cur1 = cur.next
        while cur1 != None:
            if cur.val == cur1.val:
                prev.next = cur1.next
            else:
                prev = cur1
            cur1 = cur1.next
        cur = cur.next

    return newHead

def removeDuplicatesBuffer(head):
    if head == None or head.next == None:
        return head

    h = {}
    newHead = head
    prev = None
    while head != None:
        if head.val not in h:
            h[head.val] = 1
            prev = head
        else:
            prev.next = head.next
        head = head.next
    return newHead

def display(root):
    if root == None:
        return

    head = root
    while head != None:
        print head.val,
        head = head.next

head = None
head = insert(head, 1)
head = insert(head, 1)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 3)
head = insert(head, 4)
head = insert(head, 2)

display(head)
print "\n\n"

#head = removeDuplicates(head)
head = removeDuplicatesBuffer(head)
display(head)
