from typing import List, Optional

class Solution:
    def mergeSort(self, nums: Optional[List[int]]) -> Optional[List[int]]:
        if not nums:
            return
        
        if len(nums) == 1:
            return nums
        
        # Split the array into two halves
        left = self.mergeSort(nums[0:len(nums) // 2])
        right = self.mergeSort(nums[len(nums) // 2:])
        
        # Merge the two sorted halves
        return self.merge(left, right)

    
    def merge(self, a: List[int], b: List[int]) -> List[int]:
        ans = []
        pointer_a = pointer_b = 0
        
        # Merge the two lists
        while pointer_a < len(a) and pointer_b < len(b):
            if a[pointer_a] < b[pointer_b]:
                ans.append(a[pointer_a])
                pointer_a += 1
            else:
                ans.append(b[pointer_b])
                pointer_b += 1
                
        # Append remaining elements from a
        while pointer_a < len(a):
            ans.append(a[pointer_a])
            pointer_a += 1
        
        # Append remaining elements from b
        while pointer_b < len(b):
            ans.append(b[pointer_b])
            pointer_b += 1
            
        return ans
