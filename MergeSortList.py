class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def link_list(val):
    head = tail = None
    for v in val:
        n = node(v)
        if head == None:
            head = tail = n
        else:
            tail.next = n
            tail = n
    return head

def merge(l1, l2):
    temp = node(0)
    tail = temp
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return temp.next

def display(head):
    while head:
        print(head.data, end = "->")
        head = head.next
    print("None")

a = link_list([1, 3, 5])
b = link_list([2, 4, 6])
display(merge(a, b))