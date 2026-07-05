# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = ListNode(0, None)
        result = l3
        carryover = 0

        while (l1 != None or l2 != None) or (carryover != 0):
            sumNode = 0
            if l1 == None and l2 != None:
                sumNode = 0 + l2.val
            elif l2 == None and l1 != None:
                sumNode = l1.val + 0
            elif l1 != None and l2 != None:
                sumNode = l1.val + l2.val
            print(f"sumNode:{sumNode}")

            digit = ((sumNode % 10) + carryover) % 10
            carryover = (sumNode + carryover) // 10
            print(f"digit: {digit}, carryover: {carryover}")
            print(f"l3.val: {l3.val}")
            l3.next = ListNode(digit)
            l3 = l3.next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next 

        result = result.next
        return result

