# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # Convert linked list to array
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        # Initialize a dictionary to store the sum of values at each index
        sum_dict = {-1: 0}  # Initialize with sum 0 at index -1
        cur_sum = 0
        left = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            if cur_sum in sum_dict.values():
                for key, value in sum_dict.items():
                    if value == cur_sum:
                        for j in range(key+1, i):
                            print(sum_dict, key)
                            if j in sum_dict:
                                del sum_dict[j]
                            else:
                                continue
                        cur_sum = sum_dict[key]
                        break
            else:
                sum_dict[i] = cur_sum

            print(sum_dict)
            
        # Create a new linked list with the values corresponding to the keys in the dictionary
        new_arr = [arr[key] for key in sum_dict.keys() if key != -1]
        # Return the head of the new linked list
        return create_linked_list(new_arr)

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if len(arr) == 0:
        return []
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example input
head = create_linked_list([0,1,-1])
solution = Solution()
solution.removeZeroSumSublists(head)

    