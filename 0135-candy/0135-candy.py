class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1]*n

        if n == 1:
            return 1
        
        for i in range(1,len(ratings)):
            # if i ==0 and i+1 <len(ratings):
            #     if ratings[i] > ratings[i+1]:
            #         ans[i] = ans[i] + 1
            #     else:
            #         continue
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                if ans[i] <= ans[i+1]:
                    ans[i] = ans[i+1] + 1

        
        return sum(ans)

   
# 1,2,87,87,87,2,1
# 1,2,3,1,3,2,1

# 5,4,3,2,1
# 5,4,3,2,1

# 1,2,4,3,2
# 1,2,3,1,1