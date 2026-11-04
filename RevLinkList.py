class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def link_list(list):
    head = tail = None
    for l in list:
        n = node(l)
        if head == None:
            head = tail = n
        else:
            tail.next = n
            tail = n
    return head

def reverse(head):
    curr, prev = head, None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev

def display(head):
    curr = head
    while curr:
        print(curr.data, end = "->")
        curr = curr.next
    print("None")

head = link_list([1, 2, 3, 4])
display(head)
display(reverse(head))