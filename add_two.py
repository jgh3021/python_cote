import time

def log_time(function):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print('function: {}, time : {}'.format(function.__name__, end_time-start_time))
        return result
    return wrapper_fn


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node



class Solution:
    def __init__(self):
        self.head = None
    
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    @log_time
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curn = l1
        num = 1
        first_number = 0
        while curn:
            first_number += curn.val * num
            curn = curn.next
            num *= 10
        
        curn = l2
        num = 1
        second_number = 0
        while curn:
            second_number += curn.val * num
            curn = curn.next
            num *= 10
        
        num = first_number + second_number
        head = None
        for i in reversed(str(num)):
            print(head)
            if not head:
                head = ListNode(int(i))
                curn = head
            else:
                curn.next = ListNode(int(i))
                curn = curn.next
        
        return head

l1 = Solution()
l1.insert(ListNode(3))
l1.insert(ListNode(4))
l1.insert(ListNode(5))

l2 = Solution()
l2.insert(ListNode(5))
l2.insert(ListNode(2))
l2.insert(ListNode(6))

res = Solution()

result = res.addTwoNumbers(
print(result)
