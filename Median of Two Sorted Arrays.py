##Brute Force method using Merge Sort

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         left = 0
         right = 0
         combined = []
         while left < len(nums1) and right < len(nums2):
            if nums1[left]<nums2[right]:
                combined.append(nums1[left])
                left+=1
            else:
                combined.append(nums2[right])
                right+=1
         while left<len(nums1):
            combined.append(nums1[left])
            left+=1
         while right<len(nums2):
            combined.append(nums2[right])
            right+=1
         total = len(combined) + 1

         if len(combined) % 2 == 0:
                mid = len(combined)//2
                sums = combined[mid - 1] + combined[mid] 

                return float(sums/2)
         
         return float(total/2)
