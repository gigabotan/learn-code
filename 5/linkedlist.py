
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self, val=0):
        self.start = ListNode(val)
        self.last = self.start
        self.length = 1

        self.current = self.start
    
    def len(self):
        return self.length

    def get(self, key):
        if key > self.length + 1:
            print('Out of range')
            return None

        i = 0
        cur_node = self.start

        while(i < key):
            i += 1
            cur_node = cur_node.next
        
        return cur_node

    def append(self, value):
        self.last.next = ListNode(value)
        self.last = self.last.next
        self.length += 1

    def pop(self):
        if self.length == 1:
            print('No more pop pls')
            return self.start.val

        prev = self.start
        while(prev.next != self.last):
            prev = prev.next
        
        result = self.last.val
        prev.next = None
        self.last = prev
        self.length -= 1

        return result

    def __getitem__(self, key):
        return self.get(key)


    def __next__(self):
        result = self.current

        if self.current is None:
            raise StopIteration()
        
        self.current = self.current.next

        return result


    
    def __iter__(self):
        return self



def test_generator():
    for i in range(10):
        yield i

for i in test_generator():
    print(i)


newlist = LinkedList(1)

newlist.append(2)
newlist.append(3)

print(newlist.get(0).val)
print(newlist.get(1).val)
print(newlist.get(2).val)


print(newlist[0].val)


needed_node = newlist.get(3)
if needed_node is not None:
    print(needed_node.val)
else:
    print('No value')

print('==============================')
print('Iterator test')

for node in newlist:
    print(node.val)

















# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

# class Solution:
#     def reverseList(self, llist):
#         return