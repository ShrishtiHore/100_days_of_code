#these are list nodes and hence cannot use '+' and 'sort'
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        #convert list into array
        while list1:
            arr.append(list1.val)
            list1 = list1.next
        while list2:
            arr.append(list2.val)
            list2 = list2.next
        arr.sort()
        #rebuild the linked list
        dummy = ListNode(0)
        curr = dummy
        for v in arr:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
