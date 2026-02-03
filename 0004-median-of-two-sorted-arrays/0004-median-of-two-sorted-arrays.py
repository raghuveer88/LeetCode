class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A = nums1
        B = nums2
        m,n = len(A),len(B)

        if m>n:
            A,B = B,A
            m,n = n,m
        
        total = m+n
        half = (total+1) //2
        l = 0
        r = m
        
        while l <=r:
            i = (l+r)//2
            j = half-i

            Aleft = A[i-1] if i>0 else float("-inf") 
            Aright = A[i] if i <m else float("inf")
            Bleft = B[j-1] if j >0 else float("-inf")
            Bright = B[j] if j <n else float("inf")


            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            if Aleft > Bright:
                r = i-1
            else:
                l = i+1
        
        return 0
