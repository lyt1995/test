# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        iters=1
        num1=0
        num2=0
        while(l1!=None or l2!=None):
            if l1 != None:
                num1+=l1.val*iters
                l1=l1.next
            if l2 != None:
                num2+=l2.val*iters
                l2=l2.next
            iters *= 10
        result=num1+num2
        q=None
        p=None
        head=None
        if result == 0:
            return ListNode(0)
        else:
            while(result>0):
                num = result%10
                result /= 10

                p=ListNode(num)
                if q== None:
                    head=p
                    q=p
                else:
                    q.next=p
                    q=p
            return head