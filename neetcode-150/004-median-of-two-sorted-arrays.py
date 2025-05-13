class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 # To take shorter array as nums1 on which we move index acc to binary search
        
        n1 = len(nums1)
        n2 = len(nums2)
        l,r = 0, n1 # Not Usiing indexes. We are using Number of Elements on the left side of cut hence n1 NOT n1-1
        while l<=r:
            pX = (l+r)//2
            pY = (n1+n2+1)//2 - (pX)

            L1 = float('-inf') if pX == 0 else nums1[pX-1]
            L2 = float('-inf') if pY == 0 else nums2[pY-1]
            R1 = float('inf') if pX == n1 else nums1[pX]
            R2 = float('inf') if pY == n2 else nums2[pY]

            if L1 <= R2 and L 2<= R1:
                if (n1+n2)%2 == 0:
                    return ((max(L1,L2) + min(R1,R2))/2)
                else:
                    return max(L1,L2)
            elif L1>R2:
                r = pX-1
            else:
                l = pX+1
