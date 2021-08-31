def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = 0 
        count, countl1, countl2 = 0, 0, 0
        
        temp_l1,  temp_l2 = l1, l2
        
        while l1:
            countl1 += 1
            ptrl1 = l1
            l1 = l1.next
        while l2:
            countl2 += 1
            ptrl2 = l2
            l2 = l2.next
            
        if countl1 > countl2:
            count = countl1
            short = countl1 - countl2
            for i in range(short):
                l2 = ListNode(0)
                ptrl2.next = l2
                ptrl2 = l2
        elif countl1 < countl2:
            count = countl2
            short = countl2 - countl1
            for i in range(short):
                l1 = ListNode(0)
                ptrl1.next = l1
                ptrl1 = l1
        else:
            count = countl1
        
        l1, l2 = temp_l1, temp_l2
        
        for cnt in range(count):
            place = 10**cnt
            sum = l1.val + l2.val
            value += sum*place
            l1, l2 =  l1.next, l2.next
            
            
        ptr = None
        for i in str(value):
            l3 = ListNode(i)
            l3.next = ptr
            ptr = l3
        
        return l3