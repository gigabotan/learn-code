class LinkedList:


    def __init__(self):
        pass

    
    def len(self):
        pass

    def get(self, key):
        pass

    def append(self, value):
        pass

    def pop(self, value):
        pass


test_list = LinkedList()

for i in test_list:
    print(i)





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_last_node(linkedlist):
    last_node = linkedlist
    while(last_node.next != None):
        last_node = last_node.next
    
    return last_node


def get_item(linkedlist, key):
    i = 0
    cur_node = linkedlist

    while(i < key):
        i += 1
        cur_node = cur_node.next

        if cur_node is None:
            print('Out of range')
            break
    
    return cur_node
        


def append(linkedlist, value):
    new_node = ListNode(value)

    last_node = get_last_node(linkedlist)
    last_node.next = new_node



simplelist = ListNode(1)

append(simplelist, 2)
append(simplelist, 3)

print(simplelist.val)
print(simplelist.next.val)
print(simplelist.next.next.val)

needed_node = get_item(simplelist, 3)
if needed_node is not None:
    print(needed_node.val)
else:
    print('No value')



















# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

# class Solution:
#     def reverseList(self, llist):
#         return