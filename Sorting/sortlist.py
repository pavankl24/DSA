class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        step = 1
        while step < length:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)
                prev.next = self.merge(left, right)
                while prev.next:
                    prev = prev.next
            step *= 2
            
        return dummy.next

    def split(self, head, step):
        i = 1
        while head and i < step:
            head = head.next
            i += 1
        if not head:
            return None
        next_part = head.next
        head.next = None
        return next_part

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
